# Live Demo Commands

#### Table of Contents

<!-- TOC -->

- [LocalStack Demo](#localstack-demo)
- [Workflow #1: Interacting with S3](#workflow-1-interacting-with-s3)
- [Workflow #2: Working with DynamoDB](#workflow-2-working-with-dynamodb)
- [Workflow #3: Queueing with SQS](#workflow-3-queueing-with-sqs)

<!-- /TOC -->

## LocalStack Demo

```bash
# Go into directory
cd demo

# See running containers
docker ps

# Start LocalStack
docker run --rm -p 4566:4566 localstack/localstack

# Let’s use the AWS CLI to interact with localstack
# Let’s see what s3 buckets we have
aws --endpoint-url http://0.0.0.0:4566 s3 ls

# No buckets, so let’s create one
aws --endpoint-url http://0.0.0.0:4566 s3 mb s3://demo-bucket
aws --endpoint-url http://0.0.0.0:4566 s3 ls

# Introduce awslocal

# Now we’ll create a file
echo "Hello Python Web Conference" >> greeting.txt
cat greeting

# Upload to S3
awslocal s3 cp greeting.txt s3://demo-bucket/greeting.txt

# Show it’s there
awslocal s3 ls s3://demo-bucket

# Download file and show it’s there with an `ls` and `cat`
awslocal s3 cp s3://demo-bucket/greeting.txt ./new_greeting.txt
ls
cat new_greeting.txt

# And that’s s3, we’re just scratching the surface of what you can do with localstack.

# Close down localstack by stopping the container
```

## Workflow #1: Interacting with S3

```bash
```

## Workflow #2: Working with DynamoDB

- pynamodb
- show using aws viewer and other viewer

```bash
# show things
```

## Workflow #3: Queueing with SQS

- worker prints out what's up

```bash
```
