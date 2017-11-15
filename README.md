# `guestbook`

A _serverless_ guestbook using AWS Lambda.

## Installation


### Run `script/bootstrap`

```bash
script/bootstrap
script/pack_lambda .
script/push_lambda guestbook_add package.zip
script/push_lambda guestbook_list package.zip
```

This will:

1. Ensure the Lambda function role is created, with the correct policy attached
1. Create the DynamoDB table
1. Package the Lambda function and all its dependencies
1. Create the Lambda functions, `guestbook_add` and `guestbook_list`, on AWS

## Usage

Use the `script/exec_lambda` script.

E.g. to create an entry in the guestbook:

```bash
# Create an entry in the guestbook
script/exec_lambda guestbook_add '{"name":"Florian", "message":"I program my home computer, beam myself into the future"}'
```

And to list today's guestbook entries:

```bash
# List today's guestbook entries
script/exec_lambda guestbook_list
```
