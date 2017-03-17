__author__ = 'manishankargoswami'

import os

import psutil
import distutils.util
import configparser

from config.modelConfiguration import models, features
from src.engine.core.model import Model
from src.engine.promiselog import logger
from src.engine.utils.s3 import S3

from config.serverconfig import config as primary_config
from src.engine.plugins.plugin_controller import PluginController


class Models(object):
    def __init__(self):
        config = configparser.RawConfigParser()
        config.read(primary_config['server.model.config.path'])
        self.__models = {}

        # if s3 is not enabled, it is assumed that the model is already available at the local path
        if distutils.util.strtobool(config.get('storage', 'storage.s3.enabled')):
            S3(config).download()

        local_path = config.get('models', 'model.download.location.local')
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

    def predict(self, dimensions):
        model = dimensions['model']
        logger.info("received request for model: " + model)

        if model not in features:
            raise ValueError("Given model name: " + model + "not found")

        featureproperties = features[model]['feature_properties']
        logger.debug("feature properties and window properties extracted")

        prediction = self.__models[model].predict(featureproperties, dimensions)
        logger.debug("response from model received..about to hand-off to plugin..")
        plugin = PluginController()
        return plugin.handoff_to_plugin(prediction, features[model])

    def enum(**enums):
        return type('Enum', (), enums)

    def getresourceutilization(self):
        current_process = psutil.Process(os.getpid())
        mem = current_process.memory_percent()
        for child in current_process.children(recursive=True):
            mem += child.memory_percent()
        return mem
