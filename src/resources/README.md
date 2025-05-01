**TODO:** Deploy with GitHub actions workflow

Deploy S3 buckets using CloudFormation:
```
aws cloudformation deploy \
  --stack-name sip-resources-s3-dev \
  --profile hatter \
  --template-file src/resources/s3.yaml \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --region us-west-1 \
  --parameter-overrides \
    ENVIRONMENT=dev
```

Deploy DynamoDB tables using CloudFormation:

> Dynamodb tables better to deploy separately, since it's more secure to have them in a different stack.

```
aws cloudformation deploy \
  --stack-name sip-resources-dynamodb-dev \
  --profile hatter \
  --template-file src/resources/dynamodb.yaml \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --region us-west-1 \
  --parameter-overrides \
    ENVIRONMENT=dev
```
