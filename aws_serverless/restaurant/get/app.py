"""
This lambda takes as input a session id, and returns a list of all restaurant
data for the session.
"""
import json
import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    """
    Queries the Grubfinder_Restaurant table for all items with a matching session id

    Parameters
        event (dict): Data passed from lambda for processing.
        context (dict): The lambda invocation data.

    Return
        dict: The http status code and restaurant data.
    """

    data = json.loads(event['body'])

    session_id = int(data["session_id"])
    # session_id = 685234 # For testing

    dynamodb = boto3.resource('dynamodb')
    try:
        table = dynamodb.Table('Grubfinder_Restaurant')

        response = table.query(KeyConditionExpression=Key('session_id').eq(session_id))

        items = response['Items']

    except (dynamodb.Client.exceptions.InternalServerError,
            dynamodb.Client.exceptions.ResourceNotFoundException) as e:
        print('ERROR: unable to fetch restaurants: ' + str(e))

        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Unable to get restaurants due to a server error.'
            }),
        }

    if bool(items):
        return {
            'statusCode': 200,
            'body': json.dumps(items, default=default_json),
        }

    print('ERROR: No restaurants found.')
    return {
        'statusCode': 204,
        'body': json.dumps({
            'message': 'No restaurants found.'
        }),
    }


def default_json(text):
    """JSON decoder to convert non-string json values into string"""
    return f'{text}'
