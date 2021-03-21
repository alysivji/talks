import boto3

BUCKETS_TO_CREATE = [
    "example-bucket"
]

s3_client = boto3.client('s3')
for bucket_name in BUCKETS_TO_CREATE:
    s3_client.create_bucket(Bucket=bucket_name)
