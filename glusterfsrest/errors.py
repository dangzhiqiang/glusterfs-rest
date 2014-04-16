# -*- coding: utf-8 -*-
"""
    errors.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

from flask import jsonify
from restapp import app


def resp_error(code, error):
    message = {
        'ok': False,
        'error': error
    }
    resp = jsonify(message)
    resp.status_code = code
    return resp


@app.errorhandler(404)
def not_found(error):
    return resp_error(404, str(error))


@app.errorhandler(403)
def forbidden(error):
    return resp_error(403, str(error))
