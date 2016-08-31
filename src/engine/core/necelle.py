__author__ = 'manishankargoswami'
"""
This is a wrapper class which unwinds the request and validates,
responds with error code if it sees an issue with request, else
hands over the request to one of the models.

v0.0.1
"""

from src.engine.core.models import Models
from src.engine.promiselog import logger
import os


class Necelle(object):
    def __init__(self):
        current_path=os.getcwd()        # Current working directory
        self.__models = Models(current_path)

    def promise(self, message):
        promise = self.__models.promise(message['features'])
        logger.info(promise)
        return promise

    # only basic validations
    def validaterequest(self, message):
        if 'features' not in message:
            return False

        if 'model' not in message['features']:
            return False

        return True
