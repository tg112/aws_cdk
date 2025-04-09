from aws_cdk import (
    Stack,
    aws_s3,
    aws_cloudfront
)
from constructs import Construct

class WebDeployStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "WebDeployQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
