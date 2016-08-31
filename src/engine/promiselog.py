__author__ = 'manishankargoswami'

"""
Control all logs related settings on this file

v0.0.1
"""

import logging
from logging.handlers import TimedRotatingFileHandler
from config.logconfig import config


class PromiseLog(object):
    def __init__(self):
        self.__logger = logging.getLogger("Promise Rotating Log")
        self.__logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s',
                                      datefmt='%m-%d %H:%M')

        handler = TimedRotatingFileHandler(config['promise.app.log.path'],
                                           when="h",
                                           interval=config[
                                               'promise.rotation.interval.in.hours'],
                                           backupCount=5)
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)

    def getlog(self):
        return self.__logger


logger = PromiseLog().getlog()  # do not remove this line

accessloghandlers = [TimedRotatingFileHandler(config['promise.access.log.path'], 'h', config[
    'promise.rotation.interval.in.hours']), ]  # do not remove this line
