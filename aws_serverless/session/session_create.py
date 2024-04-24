'''
This Lambda is responsible for creating a session and writing it to RDS.
'''
import json
from datetime import datetime
import boto3
import session_service

def lambda_handler(event, context):
    '''
    The actual lambda.
    '''
    data = json.loads(event['body'])

    try:
        response = session_service.yelp_search(data)

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


    session_id = session_service.create_random_id()

    restaurants = []

    for business in businesses:
        # parse transactions
        has_pickup, has_delivery = session_service.parse_transactions(business['transactions'])

        # get image urls
        image_urls = session_service.get_images(business['alias'])

        image_urls_dynamodb_format = [{'S': url} for url in image_urls]

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
                    'has_pickup': {'BOOL': has_pickup},
                    'has_delivery': {'BOOL': has_delivery},
                    'vote_count': {'N': str(0)},
                    'image_urls': {'L': image_urls_dynamodb_format}
                }
            }
        })

    transaction_request = {'TransactItems': [
            {
                'Put': {
                    'TableName': 'Grubfinder_Session',
                    'Item': {
                        'session_id': {'N': str(session_id)},
                        'host_pin': {'S': str(data['pin'])},
                        'is_closed': {'BOOL': False},
                        'created_at': {'S': datetime.now().isoformat()},
                        'vote_count': {'N': str(0)},
                    }
                }
            }
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
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        'body': json.dumps({
                'session_id': session_id,
        }),
    }
