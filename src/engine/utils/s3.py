__author__ = 'manishankargoswami'

import src.engine.utils.toolbox as tb
import configparser
import boto3
from boto3.s3.transfer import S3Transfer


class S3(object):
    def __init__(self, config):
        self._config = config
        print('aws_id: ' + config.get('s3', 's3.aws.access.key.id'))
        print('aws_key: ' + config.get('s3', 's3.aws.secret.access.key'))

        self._client = boto3.client('s3', aws_access_key_id=config.get('s3', 's3.aws.access.key.id'),
                                    aws_secret_access_key=config.get('s3', 's3.aws.secret.access.key'))
        self._transfer = S3Transfer(self._client)

    def download(self):
        files = self._config.get('models', 'model.location.files')
        local_path = self._config.get('models', 'model.download.location.local')
        file_list = files.split(",")
        self._load_from_s3(file_list, local_path)

    def _load_from_s3(self, object_list, local_path):
        primary = self._config.get('models', 'model.location.primary')

        bucket = self._config.get('s3', 's3.bucket')
        key = self._config.get('s3', 's3.key')

        for obj in object_list:
            print("key: " + key)
            print("bucket: " + bucket)
            print("local_path: " + local_path)
            self._transfer.download_file(bucket, key + obj, local_path + obj)
            tb.unzip(local_path + obj, local_path)
