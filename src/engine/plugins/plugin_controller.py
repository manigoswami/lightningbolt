__author__ = 'manishankargoswami'
"""
This is a plugin handler which allows one to add their own plugins to the service

v0.0.1
"""

from src.engine.promiselog import logger

class PluginController(object):

    def __init__(self):
        self.__plugin = None

    """
    This is primary interface which hands-off the call to a custom plugin based on
     configuration.

    """

    def __get_class(self, kls ):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__( module )
        for comp in parts[1:]:
           m = getattr(m, comp)
        return m

    def handoff_to_plugin(self, prediction, plugin_properties):
        logger.debug("plugin received the request")
        clazz = plugin_properties['plugin']['class']
        logger.debug("class extracted")

        klass = self.__get_class(clazz)
        self.__plugin = klass(prediction, plugin_properties)
        logger.debug("klass created")
        logger.debug("self.__plugin initialized")

        # the custom plugin must return back a valid dictionary instance or a json response back
        return self.__plugin.customize()

