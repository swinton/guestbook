import boto3
import datetime
import time
from decimal import Decimal


now = datetime.datetime.utcnow()
today = now.replace(hour=0, minute=0, second=0, microsecond=0)

timestamp = Decimal((now - \
    datetime.datetime(1970, 1, 1)).total_seconds())
today = Decimal((now.replace(hour=0, minute=0, second=0, microsecond=0) - \
    datetime.datetime(1970, 1, 1)).total_seconds())

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Guestbook')

table.put_item(
   Item={
       'date': today,
       'time': timestamp,
       'name': 'Steve',
       'message': datetime.datetime.utcnow().isoformat(),
    }
)
