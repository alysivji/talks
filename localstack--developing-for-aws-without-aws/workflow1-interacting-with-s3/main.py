"""
Workflow #1: Interacting with S3

Example adapted from
    - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
"""

import logging
import boto3
from botocore.exceptions import ClientError

def upload_file_to_s3(file_name, bucket, object_name=None, use_localstack=False):
    import pdb; pdb.set_trace()
    kwargs = {}
    if use_localstack:
        kwargs["endpoint_url"] = "http://0.0.0.0:4566"

    s3_client = boto3.client('s3', **kwargs)

    if object_name is None:
        object_name = file_name

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
