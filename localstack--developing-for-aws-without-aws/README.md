# LocalStack: Developing for AWS without AWS

#### Table of Contents

## Talk Description

Amazon Web Services (AWS) has over 175 managed services: from leveraging S3 as a storage bucket to developing voice-enabled applications with Alexa, developers can solve complex problems with a few API calls. You pay Amazon a little more and you ship products a lot faster.

The question isn't should you use managed services, but how best to bring them into your organization's existing processes and workflows. You probably already have one, or more than one, AWS account to support different development environments. Setting up new resources for each team/developer to test against is going to be a lot of work related to IAM roles, policies, and permissions. Also, API calls are not free; development and testing workflows that use AWS resources cost money.

Enter LocalStack. LocalStack is a testing framework used to develop cloud-native applications. Start a container and write code against a local environment that has the same functionality and APIs as AWS! This talk will discuss how to integrate LocalStack into your project by demonstrating several basic and advanced workflows. The session is geared towards intermediate and advanced developers that use AWS.

## Media

- [Slides]()

## Resources

- GitHub: [localstack/localstack](https://github.com/localstack/localstack#configurations)
  - main localstack repo
- GitHub: [localstack/awscli-local](https://github.com/localstack/awscli-local)
  - does an `alias awslocal=aws --endpoint-url=http://0.0.0.0:4566`
