import boto3

s3_client = boto3.client('s3')


def fetch_html(bucket, index_key="index.html"):
    response = s3_client.get_object(Bucket=bucket, Key=index_key)
    return {
        "html": response["Body"].read().decode('utf-8'),
        "headers": response["ResponseMetadata"]["HTTPHeaders"],
        "status":  response["ResponseMetadata"]["HTTPStatusCode"]
    }
