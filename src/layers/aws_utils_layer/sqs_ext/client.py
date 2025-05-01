import json
import boto3


class SQSMessageSender:
    """
    Sends messages to an AWS SQS queue (FIFO or standard).

    Attributes:
        queue_url (str): The URL of the target SQS queue.
        region_name (str): AWS region name for the SQS client.
        fifo (bool): Whether the queue is FIFO.
        distributor: Object that implements .next()
            and returns a valid MessageGroupId (required for FIFO Queues).
    """

    def __init__(
        self,
        queue_url: str,
        region_name: str = "us-west-1",
        fifo: bool = False,
        distributor=None,
    ):
        self.queue_url = queue_url
        self.region_name = region_name
        self.fifo = fifo
        self.distributor = distributor

        self.client = boto3.client("sqs", region_name=region_name)

    def _verify_distributor(self):
        if self.fifo and self.distributor is None:
            raise ValueError("FIFO queues require a MessageGroupId distributor.")

    def send_message(self, body: dict) -> dict:
        """
        Sends a single message to the SQS queue. Includes MessageGroupId if FIFO queue.

        Args:
            body (dict): The message payload to send.

        Returns:
            dict: The response from the SQS send_message call.
        """
        params = {
            "QueueUrl": self.queue_url,
            "MessageBody": json.dumps(body),
        }

        if self.fifo:
            self._verify_distributor()
            message_group_id = self.distributor.next()
            params["MessageGroupId"] = message_group_id

        return self.client.send_message(**params)
