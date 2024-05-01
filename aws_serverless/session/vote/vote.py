"""
This lambda handles adding votes to a session.
"""
import json
import boto3


def lambda_handler(event, context):
    """
    Queries the Grubfinder_Restaurant table for all items with a matching session id

    Parameters
        event (dict): Data passed from lambda for processing.
        context (dict): The lambda invocation data.
    """

    if event['body'] is None:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({
                'message': 'Empty request'
            }),
        }

    data = json.loads(event['body'])

    session_id = event['pathParameters']['session_id']

    transaction_items = []

    for restaurant_id, vote in data.items():
        if vote is True:
            transaction_items.append(
                {
                    'Update': {
                        'TableName': 'Grubfinder_Restaurant',
                        'Key': {
                            'session_id': {'N': session_id},
                            'restaurant_id': {'S': str(restaurant_id)},
                        },
                        'ConditionExpression': 'session_id = :s',
                        'UpdateExpression': 'ADD vote_count :i',
                        'ExpressionAttributeValues': {
                            ':i': {'N': '1'},
                            ':s': {'N': session_id}
                        }
                    }
                }
            )

    if len(transaction_items) > 0:

        transaction_items.append({
            'Update': {
                'TableName': 'Grubfinder_Session',
                'Key': {
                    'session_id': {'N': session_id},
                },
                'ConditionExpression': 'session_id = :s',
                'UpdateExpression': 'ADD vote_count :i',
                'ExpressionAttributeValues': {
                    ':i': {'N': '1'},
                    ':s': {'N': session_id}
                }
            }
        })

        try:
            dynamodb = boto3.client('dynamodb')
            dynamodb.transact_write_items(**{'TransactItems': transaction_items})
        except dynamodb.exceptions.TransactionCanceledException as e:
            print('ERROR: unable to append votes to session: ' + str(e))
            return {
                'statusCode': 500,
                'headers': {
                    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'OPTIONS,POST'
                },
                'body': json.dumps({
                    'message': 'error submitting votes'
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
            'message': 'Votes submitted'
        }),
    }


def default_json(text):
    """JSON decoder to convert non-string json values into string"""
    return f'{text}'
