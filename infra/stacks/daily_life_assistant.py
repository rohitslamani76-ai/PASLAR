from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_apigatewayv2 as apigw,
    aws_apigatewayv2_integrations as integrations,
    aws_cognito as cognito,
    aws_s3 as s3,
)
from constructs import Construct
import pathlib


class DailyLifeAssistantStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs
    ):
        super().__init__(scope, construct_id, **kwargs)

        # 1. Cognito
        user_pool = cognito.UserPool(
            self,
            "UserPool",
            sign_in_aliases=cognito.SignInAliases(email=True),
            self_sign_up_enabled=True,
            password_policy=cognito.PasswordPolicy(
                min_length=8
            ),
        )

        app_client = user_pool.add_client(
            "AppClient",
            auth_flows=cognito.AuthFlow(
                user_password=True,
                custom=True
            ),
            generate_secret=False,
        )

        # 2. S3 temporary image bucket
        temp_bucket = s3.Bucket(
            self,
            "TempImageBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            lifecycle_rules=[
                s3.LifecycleRule(
                    expiration=Duration.minutes(12)
                )
            ],
        )

        # 3. Lambda
        api_lambda = _lambda.Function(
            self,
            "ApiLambda",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="app.main:handler",
            code=_lambda.Code.from_asset(
                str(pathlib.Path(__file__).parents[2])
            ),
            timeout=Duration.seconds(30),
            environment={
                "BUCKET_NAME": temp_bucket.bucket_name,
                "USER_POOL_ID": user_pool.user_pool_id,
                "APP_CLIENT_ID": app_client.user_pool_client_id,
            },
        )

        temp_bucket.grant_read_write(api_lambda)
        user_pool.grant(api_lambda, "cognito-idp:*")

        # 4. API Gateway
        http_api = apigw.HttpApi(
            self,
            "HttpApi",
            cors_preflight=apigw.CorsPreflightOptions(
                allow_headers=["*"],
                allow_methods=[apigw.CorsHttpMethod.ANY],
                allow_origins=["*"],
            ),
        )

        integration = integrations.HttpLambdaIntegration(
            "ApiIntegration",
            api_lambda
        )

        http_api.add_routes(
            path="/{proxy+}",
            methods=[apigw.HttpMethod.ANY],
            integration=integration,
        )