"""
This lambda returns a restaurant by id.
"""
import json
import boto3
import botocore.exceptions
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    """
    Gets a Grundfinder restaurant by id.

    Parameters
        event (dict): Data passed from lambda for processing.
        context (dict): The lambda invocation data.
    """

    session_id = int(event['pathParameters']['session_id'])
    restaurant_id = event['pathParameters']['restaurant_id']

    dynamodb = boto3.resource('dynamodb')
    try:

        table = dynamodb.Table('Grubfinder_Restaurant')

        response = table.query(KeyConditionExpression=Key('session_id').eq(session_id) & Key('restaurant_id').eq(restaurant_id))

        items = response['Items']

    except(IndexError, botocore.exceptions.ClientError):
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'unable to get session due to a server error'
            }),
        }

    if len(items) > 0:
        return {
            'statusCode': 200,
            'body': json.dumps(items[0], default=default_json),
        }

    return {
        'statusCode': 404,
        'body': json.dumps({
            'message': 'restaurant not found'
        }),
    }


def default_json(text):
    """JSON decoder to convert non-string json values into string"""
    return f'{text}'
