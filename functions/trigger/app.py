import logging
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all


logger = logging.getLogger()
logger.setLevel(logging.INFO)
patch_all()

emr = boto3.client('emr')

def lambda_handler(event, context):
    result = {
        'id': 'a'
    }

    return result
