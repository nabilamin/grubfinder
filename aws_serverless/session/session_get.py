"""
This lambda returns a session's details.
"""
import json
import boto3
import botocore.exceptions
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    """
    Gets a Grundfinder session by id.

    Parameters
        event (dict): Data passed from lambda for processing.
        context (dict): The lambda invocation data.
    """

    session_id = int(event['pathParameters']['session_id'])

    dynamodb = boto3.resource('dynamodb')
    try:

        table = dynamodb.Table('Grubfinder_Session')

        response = table.query(KeyConditionExpression=Key('session_id').eq(session_id))

        items = response['Items']

    except(IndexError, botocore.exceptions.ClientError):
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'unable to get session due to a server error'
            }),
        }

    if len(items) == 0:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'message': 'session not found'
        }),
    }

    item = items[0]

    try:
        pin = int(event['headers']['Authorization'])

        host_pin = int(item['host_pin'])

        if pin != host_pin:
            return {
                'statusCode': 401,
                'body': json.dumps({
                    'message': 'unauthorized'
            }),
        }
        
    except KeyError:
        # unauthenticated request - do not show vote count
        del item['vote_count']
    except ValueError:
        # bad value, return unauthorized
        return {
            'statusCode': 401,
            'body': json.dumps({
                'message': 'unauthorized'
            }),
        }
    

    # do not return the host pin
    del item['host_pin']

    return {
        'statusCode': 200,
        'body': json.dumps(item, default=default_json),
    }


def default_json(text):
    """JSON decoder to convert non-string json values into string"""
    return f'{text}'
