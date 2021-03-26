import json
import logging

import boto3
from botocore.exceptions import ClientError

QUEUE_URL = "http://localhost:4566/000000000000/inbound-queue"

def send_message_to_queue(message, use_localstack=False):
    kwargs = {}
    if use_localstack:
        kwargs["endpoint_url"] = "http://0.0.0.0:4566"
    sqs = boto3.resource("sqs", **kwargs)
    queue = sqs.Queue(QUEUE_URL)

    try:
        result = queue.send_message(MessageBody=json.dumps(message))
    except ClientError as e:
        logging.error(e)
        return False
    return True
