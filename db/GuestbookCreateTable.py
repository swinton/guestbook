from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


table = dynamodb.create_table(
    TableName='Guestbook',
    KeySchema=[
        {
            'AttributeName': 'date',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'time',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'date',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'time',
            'AttributeType': 'N'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
