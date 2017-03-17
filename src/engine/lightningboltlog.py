__author__ = 'manishankargoswami'

"""
Control all logs related settings on this file

v0.0.1
"""

import logging
from logging.handlers import TimedRotatingFileHandler
from config.logconfig import config


class LightningboltLog(object):
    def __init__(self):
        self.__logger = logging.getLogger("Lightningbolt Rotating Log")
        self.__logger.setLevel(config['lightningbolt.logging.log.level'])
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s',
                                      datefmt='%m-%d %H:%M')

        handler = TimedRotatingFileHandler(config['lightningbolt.app.log.path'],
                                           when="h",
                                           interval=config[
                                               'lightningbolt.rotation.interval.in.hours'],
                                           backupCount=5)
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)

    def getlog(self):
        return self.__logger


logger = LightningboltLog().getlog()  # do not remove this line

accessloghandlers = [TimedRotatingFileHandler(config['lightningbolt.access.log.path'], 'h', config[
    'lightningbolt.rotation.interval.in.hours']), ]  # do not remove this line
