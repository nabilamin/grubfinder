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
    dynamodb = boto3.resource('dynamodb')

    try:
        session_id = int(event['pathParameters']['session_id'])

        table = dynamodb.Table('Grubfinder_Restaurant')

        response = table.query(KeyConditionExpression=Key('session_id').eq(session_id))

        items = response['Items']

    except (dynamodb.Client.exceptions.InternalServerError,
            dynamodb.Client.exceptions.ResourceNotFoundException, ValueError):

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

    return {
        'statusCode': 404,
        'body': json.dumps({
            'message': 'Session not found.'
        }),
    }


def default_json(text):
    """JSON decoder to convert non-string json values into string"""
    return f'{text}'
