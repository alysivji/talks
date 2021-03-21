import boto3

QUEUES_TO_CREATE = [
    "inbound-queue",
]

sqs = boto3.resource('sqs')
for queue_name in QUEUES_TO_CREATE:
    queue = sqs.create_queue(QueueName=queue_name})
