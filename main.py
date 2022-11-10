
import logging
import os

from flask import Flask
import redis

app = Flask(__name__)

redis_host = '10.0.0.12'
redis_port = 6379
redis_client = redis.StrictRedis(host=redis_host, port=redis_port)


@app.route('/incr')
def incr():

    value = redis_client.incr('counter', 1)
    return 'Counter incremented: {}'.format(value)

@app.route('/decr')
def decr():

    value = redis_client.decr('counter', 1)
    return 'Counter decremented: {}'.format(value)


@app.errorhandler(500)

def server_error(e):

    logging.exception('An error occurred during a request.')

    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=True)
    