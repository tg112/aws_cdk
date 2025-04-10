from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
    CfnOutput,
    Fn
)
from constructs import Construct

class CdkPracticeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        suffix = self.__initialize_suffix()

        self.bucket = s3.Bucket(self, "PyBucket",
            bucket_name=f"bucket-{suffix}",
            lifecycle_rules=[
                s3.LifecycleRule(
                    expiration=Duration.days(3),
                ),
            ]
        )
        print('Bucket name: ' + self.bucket.bucket_name)
        CfnOutput(self, 'BucketName', value=self.bucket.bucket_name)

    def __initialize_suffix(self):
        short_stack_id = Fn.select(2, Fn.split('/', self.stack_id))
        suffix = Fn.select(4, Fn.split('-', short_stack_id))
        return suffix

    @property
    def my_bucket(self):
        return self.bucket