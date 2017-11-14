from __future__ import print_function # Python 2/3 compatibility
import boto3
from boto3.dynamodb.conditions import Key, Attr
import datetime
from decimal import Decimal


now = datetime.datetime.utcnow()
today = Decimal((now.replace(hour=0, minute=0, second=0, microsecond=0) - \
    datetime.datetime(1970, 1, 1)).total_seconds())

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Guestbook')

print("Messages from today")

response = table.query(
    KeyConditionExpression=Key('date').eq(today),
    ScanIndexForward=False
)

for i in response['Items']:
    print(i['name'], ":", i['message'])
