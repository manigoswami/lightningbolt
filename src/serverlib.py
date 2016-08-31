__author__ = 'manishankargoswami'

import cherrypy as cp
from cherrypy.process.plugins import Daemonizer,PIDFile
import argparse
from cherrypy.wsgiserver import CherryPyWSGIServer
from cherrypy.process.servers import ServerAdapter


def run_decoupled(app, host='0.0.0.0', port=8080, **config):
    server = CherryPyWSGIServer((host, port), app, **config)
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()


def run_in_cp_tree(app, host='0.0.0.0', port=8080, pidfile='/tmp/',  **config):
    cp.tree.graft(app, '/')
    cp.config.update(config)
    cp.config.update({
        'server.socket_port': port,
        'server.socket_host': host
    })
    Daemonizer(cp.engine).subscribe()
    PIDFile(cp.engine, pidfile).subscribe()
    cp.engine.start()


def run_with_adapter(app, host='0.0.0.0', port=8080, config=None, **kwargs):
    cp.server.unsubscribe()
    bind_addr = (host, port)
    cp.server = ServerAdapter(cp.engine,
                              CherryPyWSGIServer(bind_addr, app, **kwargs),
                              bind_addr).subscribe()
    cp.config.update({
        'global': {
            'engine.autoreload.on': False
        }
    })
    if config:
        cp.config.update(config)
    cp.engine.signals.subscribe()  # optional
    cp.engine.start()
    cp.engine.block()
