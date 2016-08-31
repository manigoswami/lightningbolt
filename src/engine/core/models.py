__author__ = 'manishankargoswami'

import os

import psutil

from config.modelConfiguration import models, features
from src.engine.core.model import Model
from src.engine.promiselog import logger
from src.engine.utils.s3 import S3
import configparser


class Models(object):
    def __init__(self,path):
        config = configparser.RawConfigParser()
        config_path=path+'/../config/model.properties'
        config.read(config_path)
        self.__models = {}
        S3(config).download()

        local_path = config.get('models', 'model.location.local')
        size = self.getresourceutilization()
        logger.info("init:: size so far: " + str(size))
        for model, path in models.items():
            logger.info("loading " + model + " now...")
            path = local_path + path

            self.__models[model] = Model(path)
            size = self.getresourceutilization()
            logger.info("size so far: " + str(size))
        logger.info("every thing loaded..all set to click...")

    def getmodel(self, model):
        return self.__models[model]

    def promise(self, dimensions):
        model = dimensions['model']
        logger.info("received request for model: " + model)

        if model not in features:
            raise ValueError("Given model name: " + model + "not found")

        featureproperties = features[model]['feature_properties']
        windowproperties = features[model]['window_properties']
        return self.__models[model].predict(featureproperties, windowproperties, dimensions)

    def enum(**enums):
        return type('Enum', (), enums)

    def getresourceutilization(self):
        current_process = psutil.Process(os.getpid())
        mem = current_process.memory_percent()
        for child in current_process.children(recursive=True):
            mem += child.memory_percent()
        return mem


