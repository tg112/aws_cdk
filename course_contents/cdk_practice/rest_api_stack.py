from aws_cdk import (
    Stack,
    aws_apigateway, aws_lambda,
    aws_dynamodb,
)
from constructs import Construct

class RestApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        employee_table = aws_dynamodb.TableV2(
            self,
            "EmployeeTable",
            partition_key=aws_dynamodb.Attribute(
                name="id", type=aws_dynamodb.AttributeType.STRING
            ),
            billing=aws_dynamodb.Billing.on_demand()
        )

        employee_lambda = aws_lambda.Function(
            self,
            "EmployeeLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            code=aws_lambda.Code.from_asset('services'),
            handler="index.handler",
            environment={"TABLE_NAME": employee_table.table_name},
        )

        # lambdaに権限を与える
        employee_table.grant_read_write_data(employee_lambda)

        api = aws_apigateway.RestApi(self, 'Sample-Rest-Api')

        # Corsの対応
        cors_options = aws_apigateway.CorsOptions(
            allow_origins=aws_apigateway.Cors.ALL_ORIGINS,
            allow_methods=aws_apigateway.Cors.ALL_METHODS,
        )

        employees_resource = api.root.add_resource('employees', default_cors_preflight_options=cors_options)

        employee_lambda_integration = aws_apigateway.LambdaIntegration(employee_lambda)
        employees_resource.add_method('GET', employee_lambda_integration)
        employees_resource.add_method('POST', employee_lambda_integration)
