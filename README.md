# `guestbook`

A _serverless_ guestbook using AWS Lambda.

## Installation

1. Sign up for AWS Lambda
1. Install and configure the `aws` command-line client
1. Run `script/bootstrap`

### Sign up for AWS Lambda

Sign up for AWS [**here**](https://aws.amazon.com/).

The Lambda free tier includes 1M free requests per month and 400,000 GB-seconds of compute time per month.

### Install and configure the `aws` command-line client

To install the `aws` command-line client use `pip`:

```
pip install awscli --upgrade --user
```

To configure `aws`, follow these [**quick configuration steps**](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration).

Once configured, you should see `config` and `credentials` files in `~/.aws`.

### Run `script/bootstrap`

```bash
script/bootstrap
script/pack_lambda .
script/push_lambda guestbook_add package.zip
script/push_lambda guestbook_list package.zip
script/push_lambda message_add package.zip
script/push_lambda messages_received_list package.zip
script/push_lambda messages_sent_list package.zip
```

This will:

1. Ensure the Lambda function role is created, with the correct policy attached
1. Create the DynamoDB table
1. Package the Lambda function and all its dependencies
1. Create the Lambda functions, `guestbook_add`, `guestbook_list`, `message_add`, `messages_received_list`, and `messages_sent_list` on AWS

## Usage

Use the `script/exec_lambda` script.

### Guestbook

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

### Messages

To send a message:

```bash
script/exec_lambda message_add '{"toId": 2993937, "to": "imjohnbo", "fromId": 27806, "from": "swinton", "message": "Hello, John, how are you?"}'
```

To list the 50 most recently received messages:

```bash
script/exec_lambda messages_received_list '{"toId": 2993937}'
```

To list the 50 most recently sent messages:

```bash
script/exec_lambda messages_sent_list '{"fromId": 27806}'
```
