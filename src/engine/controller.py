__author__ = 'manishankargoswami'

"""
This is the primary controller which fires all engine component
and prepares itself to respond in real-time to generate promise

v0.0.1
"""

from bottle import Bottle, request, response
from requestlogger import WSGILogger, ApacheFormatter

from src.engine.promiselog import accessloghandlers
from src.engine.core.necelle import Necelle
import src.engine.utils.toolbox as tb

tb.write_to_console("starting up...hold tight..might take up to 10 to 15 minutes")
app = Bottle()
necelle = Necelle()
tb.write_to_console("loaded all models...ready to take traffic...")


@app.route('/lightningbolt/test/v1', method='POST')
def getpromise():
    if not necelle.validate_request(request.json):
        response.status = 400
        return tb.invalid_request_message()

    try:
        promise = necelle.predict(request.json)
        return promise

    except Exception as e:
        return tb.invalid_model_message(e)


app = WSGILogger(app, accessloghandlers, ApacheFormatter())
