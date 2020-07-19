import boto3
from time import time
from copy import deepcopy

cached_state = None
cache_timestamp = None
cache_ttl = 60


def fetch_html(bucket, index_key="index.html"):
    global cached_state
    global cache_timestamp
    now = time()
    if cached_state and now - cache_timestamp < cache_ttl:
        return deepcopy(cached_state)
    else:
        s3_client = boto3.client('s3')
        response = s3_client.get_object(Bucket=bucket, Key=index_key)
        state = {
            "html": response["Body"].read().decode('utf-8'),
            "headers": response["ResponseMetadata"]["HTTPHeaders"],
            "status":  response["ResponseMetadata"]["HTTPStatusCode"]
        }
        cached_state = deepcopy(state)
        cache_timestamp = now
        return state
