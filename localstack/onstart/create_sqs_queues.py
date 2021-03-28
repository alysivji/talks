import boto3

sqs = boto3.client("sqs", endpoint_url="http://0.0.0.0:4566")
queue_name = "inbound-queue"
sqs.create_queue(QueueName=queue_name)
