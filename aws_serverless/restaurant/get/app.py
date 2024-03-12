"""
This lambda is responsible for fetching a list of all restaurant data from dynamoDB.
"""
import json
import boto3

def lambda_handler(event, context):
    '''
    The actual lambda.
    '''

    data = json.loads(event['body'])

    session_id = data["session_id"]

    try:
        dynamodb = boto3.client('dynamodb')
        # TODO: write code here that fetches the data from dynamoBB table (Grubfinder_Restaurant) based on session_id.
    except dynamodb.exceptions.TransactionCanceledException as e:
        print('ERROR: unable to fetch restaurants: ' + str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'error fetching restaurants'
            }),
        }

    return {
        'statusCode': 200,
        'body': json.dumps({
                'foo': 'bar'
        }),
    }