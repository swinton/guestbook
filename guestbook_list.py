#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import datetime
import json

import boto3
from boto3.dynamodb.conditions import Key

from decimal import Decimal


def handler(event, context):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table("Guestbook")

    now = datetime.datetime.utcnow()
    today = Decimal((now.replace(hour=0, minute=0, second=0, microsecond=0) - \
        datetime.datetime(1970, 1, 1)).total_seconds())

    # Get today's Guestbook entries, most recent first
    results = table.query(
        KeyConditionExpression=Key("date").eq(today),
        ScanIndexForward=False
    )

    return [dict(name=result["name"], message=result["message"]) for result in results["Items"]]


if __name__ == "__main__":
    # Read event, context from sys.argv
    args = [json.loads(arg) for arg in sys.argv[1:2]]

    # Provide None for event, context if not provided
    while len(args) < 2:
        args.append(None)

    # Print the output
    print json.dumps(handler(*args), indent=4)
