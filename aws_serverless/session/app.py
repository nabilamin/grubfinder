'''
This Lambda is responsible for creating a session and writing it to RDS.
'''
import json
import uuid
from datetime import datetime
import boto3
import requests
from util import generate_id

def yelp_search(data):
    '''
    Executes a search against yelp's API.
    '''
    url = yelp_search_url_builder(data['location'], data['price'], data['open_at'])

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + get_yelp_key()
    }

    response = requests.get(url, headers=headers, timeout=10)

    return response


def yelp_search_url_builder(location: str, price: int, open_at: str):
    '''
    Builds the url string to get a list of restaurants from.
    '''
    base_url = f'https://api.yelp.com/v3/businesses/search?location={location}&price={price}&term=restaurants&sort_by=rating&limit=10'

    if open_at != '':
        # todo: convert time stamp to unix time per yelp api docs
        pass

    return  base_url

def get_yelp_key():
    '''
    Gets the api key from aws secret manager to use when requesting data from yelp's API.
    '''
    secret_name = 'yelp_key'
    region_name = 'us-east-1'

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    get_secret_value_response = client.get_secret_value(SecretId=secret_name)

    return json.loads(get_secret_value_response['SecretString'])['key']


def lambda_handler(event, context):
    '''
    The actual lambda.
    '''
    data = event['body']

    try:
        response = yelp_search(json.loads(data))

        if response.status_code != 200:
            return {
                'statusCode': response.status_code,
                'body': json.dumps({
                    'message': 'error getting yelp data'
                }),
            }

        businesses = response.json()['businesses']
    except KeyError as e:
        print('ERROR: failed to find key: ' + str(e))
        return {
            'statusCode': 500
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'error getting yelp data'
            }),
        }

    if len(businesses) < 5:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'not enough data'
            }),
        }


    session_id = generate_id()
    user_id = generate_id()
    host_key = str(uuid.uuid4())

    restaurants = []

    for business in businesses:
        restaurants.append({
            'Put': {
                'TableName': 'Grubfinder_Restaurant',
                'Item': {
                    'session_id': {'N': str(session_id)},
                    'restaurant_id': {'S': str(business['id'])},
                    'name': {'S': business['name']},
                    'review_count': {'N': str(business['review_count'])},
                    'rating': {'N': str(business['rating'])},
                    'address': {'S': ' '.join(business['location']['display_address'])},
                    'vote_count': {'N': str(0)}
                }
            }
        })

    transaction_request = {'TransactItems': [
            {
                'Put': {
                    'TableName': 'Grubfinder_Session',
                    'Item': {
                        'session_id': {'N': str(session_id)},
                        'host_key': {'S': host_key},
                        'is_closed': {'BOOL': False},
                        'created_at': {'S': datetime.now().isoformat()}
                    }
                }
            },
            {
                'Put': {
                    'TableName': 'Grubfinder_User',
                    'Item': {
                        'session_id': {'N': str(session_id)},
                        'user_id': {'N': str(user_id)},
                    }
                }
            },
        ]
    }

    transaction_request['TransactItems'].extend(restaurants)

    try:
        dynamodb = boto3.client('dynamodb')
        dynamodb.transact_write_items(**transaction_request)
    except dynamodb.exceptions.TransactionCanceledException as e:
        print('ERROR: unable to create session: ' + str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'error creating session'
            }),
        }

    return {
        'statusCode': 200,
        'body': json.dumps({
                'user_id': user_id,
                'host_key': host_key,
        }),
    }
