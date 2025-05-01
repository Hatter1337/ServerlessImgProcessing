import json
import logging


# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):  # noqa
    for record in event["Records"]:
        msg_body = json.loads(record["body"])
        logger.info(f"Message body: {msg_body}")

    return {
        "statusCode": 200,
        "body": f"{len(event['Records'])} records were processed successfully",
    }
