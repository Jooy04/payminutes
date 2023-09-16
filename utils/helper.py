
import boto3

access_key = 'AKIAU3WDFXA6AP4APFOK'
secret_key= '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'

region= 'ca-central-1'

bucket_name= 'payminutes'
def create_bucket():
    client = boto3.client(
        's3',
        aws_access_key_id= access_key,

        aws_secret_access_key=secret_key
    
)

    client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )