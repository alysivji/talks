import boto3

dynamodb = boto3.resource("dynamodb", endpoint_url="http://0.0.0.0:4566")
table = dynamodb.create_table(
    TableName="User",
    KeySchema=[
        {"AttributeName": "email", "KeyType": "HASH"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "email", "AttributeType": "S"},
    ],
    ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    # use ondemand on AWS if you are building this is a new table
    # monitor access patterns and usage before provisioning units
    # ondemand is a bit more expensive, but worth not having to think about
)
