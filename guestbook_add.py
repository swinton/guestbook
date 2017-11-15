#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import datetime

import boto3

from decimal import Decimal


def handler(event, context):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table("Guestbook")

    now = datetime.datetime.utcnow()
    today = Decimal((now.replace(hour=0, minute=0, second=0, microsecond=0) - \
        datetime.datetime(1970, 1, 1)).total_seconds())
    timestamp = Decimal((now - \
        datetime.datetime(1970, 1, 1)).total_seconds())

    table.put_item(
       Item={
           "date": today,
           "time": timestamp,
           "name": event["name"],
           "message": event["message"],
        }
    )

    return True


if __name__ == "__main__":
    # Read event, context from sys.argv
    args = [json.loads(arg) for arg in sys.argv[1:2]]

    # Provide None for event, context if not provided
    while len(args) < 2:
        args.append(None)

    # Print the output
    print handler(*args)
