"""
This lambda handles ending a session.
"""
import random
import json
import boto3
from boto3.dynamodb.conditions import Key

dbResource = boto3.resource('dynamodb')
dbClient = boto3.client('dynamodb')

def lambda_handler(event, context):
    """
    Ends a session and determines the winning restaurant.

    Parameters
        event (dict): Data passed from lambda for processing.
        context (dict): The lambda invocation data.
    """

    session_id = event['pathParameters']['session_id']

    transaction_items = []

    # get restaurants
    try:
        restaurant_id = caclulate_winning_restaurant(int(session_id))
    except (dbClient.exceptions.InternalServerError,
            dbClient.exceptions.ResourceNotFoundException, ValueError):
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({
                'message': 'Unable to get restaurants due to a server error.'
            }),
        }

    # appent close session transaction
    transaction_items.append({
        'Update': {
            'TableName': 'Grubfinder_Session',
            'Key': {
                'session_id': {'N': session_id},
            },
            'ConditionExpression': 'session_id = :s',
            'UpdateExpression': 'SET is_closed = :v, winning_restaurant_id = :r',
            'ExpressionAttributeValues': {
                ':s': {'N': session_id},
                ':v': {'BOOL': True},
                ':r': {'S': restaurant_id}
            }
        }
    })

    try:
        dbClient.transact_write_items(**{'TransactItems': transaction_items})
    except dbClient.exceptions.TransactionCanceledException as e:
        print('ERROR: unable to end session ' + str(e))
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({
                'message': 'error ending session'
            }),
        }

    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST'
        },
        'body': json.dumps({
            'message': 'Session ended'
        }),
    }

def caclulate_winning_restaurant(session_id: int) -> str:
    """
    Caclulate the winning restaurant
    """
    # get restaurant list
    table = dbResource.Table('Grubfinder_Restaurant')
    response = table.query(KeyConditionExpression=Key('session_id').eq(session_id))
    items = response['Items']
    # sort items
    items.sort(key=sort_restaurant_by_votes, reverse=True)
    # loop
    top_count = 0
    top_items = []
    for index, item in enumerate(items):
        if index == 0:
            top_count = item['vote_count']
        if item['vote_count'] == top_count:
            top_items.append(item)
    # select randomly from the top count
    return items[random.randrange(0, len(top_items))]['restaurant_id']


def sort_restaurant_by_votes(val):
    """
    Sort function for restaurants
    """
    return val['vote_count']


def default_json(text):
    """JSON decoder to convert non-string json values into string"""
    return f'{text}'
