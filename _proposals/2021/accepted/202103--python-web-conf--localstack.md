# LocalStack: Developing for AWS without AWS

## Description

Amazon Web Services (AWS) has over 175 managed services: from leveraging S3 as a storage bucket to developing voice-enabled applications with Alexa, developers can solve complex problems with a few API calls. You pay Amazon a little more and you ship products a lot faster.

The question isn't should you use managed services, but how best to bring them into your organization's existing processes and workflows. You probably already have one, or more than one, AWS account to support different development environments. Setting up new resources for each team/developer to test against is going to be a lot of work related to IAM roles, policies, and permissions. Also, API calls are not free; development and testing workflows that use AWS resources cost money.

Enter LocalStack. LocalStack is a testing framework used to develop cloud-native applications. Start a container and write code against a local environment that has the same functionality and APIs as AWS! This talk will discuss how to integrate LocalStack into your project by demonstrating several basic and advanced workflows. The session is geared towards intermediate and advanced developers that use AWS.

## Outline

- introduction
  - why AWS managed services are great

- introducing localstack
  - aws in a container
  - can replicate lots of services, paid version has more... if you really need them
  - benefits of localstack: https://localstack.cloud/
    - language agnostic
      - other solutions like fake_sqs and moto are for ruby and python respectively
  - cons: setting it up is a bit of a pain, but i have some lesson learned and this talk contains a few workflows to help you get started

- demo: localstack
  - show how easy it is to use
  - live code: aws cli: `aws --endpoint-url` and then pip install it and do `awslocal`
    - create buckets
    - save to bucket

- dive in local stack
  - common options, what they mean
  - demo to show how to create resources in the shell script
  - advanced localstack?
  - aside: how does it work so you have a sense of what it does

- workflow #1: website Static site s3 / Upload files
  - show Django example
  - also have flask example done
  - the s3 protocol is used by a lot of folks so you can use localstack for DigitalOcean and (Azure?)

- workflow #2: working with dynamodb
  - this is awesome, maybe we can use?

- workflow #3: working with SQS
  - we can use task queues to run tasks asynchronously
  - why set up redis when you can set up SQS
  - celery has support

- workflow #4: deploy terraform and cloudformation
  - everything we've done until now, we've done in the console... this is not the best way
  - we should use terraform

- workflow #5: developing serverless applications
  - joke: developing event-driven severless applications
  - continued joke: using cloud native technologies... get all the buzzwords in there
  - image resizer: save something to a bucket, goes thru my photos and rotates them

- i'm not here to sell on on the AWS serverless stack, my goal is to show

- Tips and Tricks
  - setting up in CI is pretty straight forward
    - included a GitHub Action; can be used as a template to create others
  - zappa is popular in the Python space since people can leverage web technologies they already know
    - this does make sense, but you also know Python
    - writing a lambda function is a lot easier than writing a web application
    - make sure you think of the use case before you jump into a full framework like Zappa, you can maybe get away with SAM / Serverless + LocalStack
    - have a comparison blog post (also examine cold start time -- zappa is bad because Django is bad. Python itself is great!)
  - commandeer?

  - what sucks about develping against managed services
    - development tools aren't as mature as server-based counterparts
      - for serverless, it's one of the reasons why Zappa is popular, even though it has so many limitations
    - testing and debugging is hard since it's difficult to replicate a production environment
    - deployment is unfamiliar
      - nothing we can do about this, but learning about localstack will increase your confidence in your cloudformation (maybe don't say this)
    - it becomes expensive, each developer is running resources on AWS and that costs money
    - what else?
