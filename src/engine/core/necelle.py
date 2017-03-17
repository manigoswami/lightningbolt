__author__ = 'manishankargoswami'
"""
This is a wrapper class which unwinds the request and validates,
responds with error code if it sees an issue with request, else
hands over the request to one of the models.

v0.0.1
"""

from src.engine.core.models import Models
from src.engine.promiselog import logger
from config.serverconfig import config


class Necelle(object):
    def __init__(self):
        self.__models = Models()

    def predict(self, message):
        prediction = self.__models.predict(message['features'])
        logger.info("Prediction being returned: " + str(prediction))
        return prediction


    def validate_request(self, message):
        if 'features' not in message:
            return False

        if 'model' not in message['features']:
            return False

        return True

    def is_premium_applicable(self):
        if not config['premium.service']:
            return False
        return True