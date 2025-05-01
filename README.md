# Serverless Image Processing

![Python 3.13](https://img.shields.io/badge/python-3.13-3776AB.svg?style=flat&logo=python&logoColor=yellow)
![SAM](https://img.shields.io/badge/SAM-v1.137.1-blue.svg)

> **SAM** template file is located in the root directory: `template.yaml` together with configuration file `samconfig.toml`.

## Local development
### Run SAM application
- `$ sam build --profile hatter`
- `$ sam local start-api --port 8000 --profile hatter`


#### Notes
- Instead of the `hatter` profile, use appropriate profile for the **aws cli** to access AWS resources.
- Ensure you have configured your **AWS CLI** with the necessary profile / credentials before running SAM commands.

## Deployment
> On the first deployment, you should deploy the resources from the `src/resources` directory.  
This will create the **S3 bucket** required for the **SAM deployment**.

Deploy the application using the following commands:
- `$ sam build`
- `$ sam deploy --config-env dev --profile hatter`

#### Notes
- Instead of the `hatter` profile, use appropriate profile for the **aws cli** to access AWS resources.
