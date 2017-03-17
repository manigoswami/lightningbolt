__author__ = 'manishankargoswami'
"""
This is a plugin handler which allows one to add their own plugins to the service

v0.0.1
"""
from src.engine.core.prediction import Prediction
import numpy as np
from src.engine.lightningboltlog import logger

class FindBestClass(object):

    def __init__(self, prediction, properties):
        self.__prediction = prediction
        self.__properties = properties


    def customize(self):
        logger.debug("request received by the actual plugin..")
        # just few example lines of code to show how a plugin can apply
        # customization to a std logic. Here for example, we are accessing a
        # probability distribution and sending out a static logic.

        weightarray = np.array(self.__prediction.get_probability_distribution()).reshape(-1, ).tolist()
        return {'min': 3, 'max': 5}