# This script can be used to test that you have SQS access

# CHANGE THESE VARIABLES
# Or set them in credentials.py
QUEUE_URL = ''
AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''

try:
    from credentials import *
except ImportError:
    pass

import boto3

sqs = boto3.client('sqs',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY)

msg_a = {
        'title': {
            'DataType': 'String',
            'StringValue': 'The title of the meeting'
        }
    }
msg_b = 'This is where additional info about the meeting could end up'

resp = sqs.send_message(
        QueueUrl=QUEUE_URL,
        DelaySeconds=10,
        MessageAttributes=msg_a,
        MessageBody=msg_b)

print(resp)
print(resp['MessageId'])

resp = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0)

message = resp['Messages'][0]
receipt_handle = message['ReceiptHandle']

sqs.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=receipt_handle)

print('Rec and deleted msg {}'.format(message))


