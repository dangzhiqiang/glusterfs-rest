# -*- coding: utf-8 -*-
"""
    restapp.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask, request, jsonify
from functools import wraps
from settings import APP_DEBUG
from glusterfsrest import users

app = Flask(__name__)
app.debug = APP_DEBUG
users.connect()


def resp_success(data):
    message = {
        'ok': True,
        'data': data
    }
    return jsonify(message)


def resp_error(code, error, headers=None):
    message = {
        'ok': False,
        'error': error
    }
    resp = jsonify(message)
    resp.status_code = code
    if headers:
        for k, v in headers.items():
            resp.headers[k] = v
    return resp


@app.errorhandler(404)
def not_found(error):
    return resp_error(404, str(error))


@app.errorhandler(403)
def forbidden(error):
    return resp_error(403, str(error))


def authenticate_error():
    """Sends a 401 response that enables basic auth"""
    return resp_error(
        401,
        'Forbidden',
        headers={'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_auth(groups=[]):
    def requires_auth_decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not users.authenticate(auth.username,
                                                  auth.password,
                                                  groups):
                return authenticate_error()
            return f(*args, **kwargs)
        return decorated
    return requires_auth_decorator


def start(host, port):
    app.run(port=port)
