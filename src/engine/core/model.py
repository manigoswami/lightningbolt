__author__ = 'manishankargoswami'
"""
This class represents a model, it does all the heavy wight-lifting
in terms of loading model, parsing the incoming request dimensions,
running prediction and generating the validation window

"""

from sklearn.externals import joblib
import numpy as np

from src.engine.utils import toolbox
from src.engine.core.prediction import Prediction
from src.engine.lightningboltlog import logger



class Model(object):
    def __init__(self, path):

        self.__model = joblib.load(path)

    def get(self):
        return self.__model

    def __getfeatures(self, featureproperties, dimensions):
        logger.debug("request received by getfeatures")
        iterations = 0
        result = 0
        features = []
        for feature, properties in featureproperties.items():
            for items in properties:

                if items == 'donothing':
                    continue
                if iterations == 0:
                    result = getattr(toolbox, items)(dimensions[feature])
                else:
                    result = getattr(toolbox, items)(result)
                iterations += 1

            features.append(result)
            result = 0
            iterations = 0

        return np.array(features)

    def predict(self, featureproperties, dimensions):
        logger.debug("request delegated to model..")
        x = self.__getfeatures(featureproperties, dimensions)
        testX = x.astype(np.float)
        logger.debug("features already extracted..ready to return")
        return Prediction(self.__model.predict(testX), self.__model.predict_proba(testX))
