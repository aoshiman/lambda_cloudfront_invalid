import time
import boto3
import lamvery

def lambda_handler(event, context):
    client = boto3.client('cloudfront')
    distributionid = lamvery.secret.get('secret')
    invalidation = client.create_invalidation(
            DistributionId=distributionid,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [
                        '/*',
                    ]
                },
            'CallerReference': str(time.time())
        }
    )
