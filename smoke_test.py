# This script can be used to test that you have SQS access

# CHANGE THESE VARIABLES
QUEUE_URL = 'SQS_QUEUE_URL'

import boto3

sqs = boto3.client('sqs')

msg_a = {
        'title': {
            'DataType': 'String',
            'StringValue': 'The title of the meeting'
        }
    }
msg_b = 'This is where additional info about the meeting could end up'

resp = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes=msg_a,
        MessageBody=msg_b)

print(resp)
print(resp['MessageId'])

resp = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle)

print('Rec and deleted msg {}'.format(message))


