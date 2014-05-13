# -*- coding: utf-8 -*-
"""
    api.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

from functools import wraps
from flask import render_template, request
from glusterfsrest.restapp import app, requires_auth, resp_success, resp_error
from glusterfsrest.cli import volume, peer


doclist = []


def api(func):
    global doclist
    if func.__doc__:
        doclist.append(func.__doc__)

    @wraps(func)
    def decorated(*args, **kwargs):
        try:
            return resp_success(func(*args, **kwargs))
        except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
            return resp_error(200, e)

    return decorated


def get_post_data(key, default_value=None):
    return request.form[key] if key in request.form else default_value


@app.route("/api/<int:version>/doc")
def showdoc(version):
    return render_template("doc.html")


@app.route("/api/<int:version>/volumes/<string:name>", methods=["POST"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_create(version, name):
    bricks_str = get_post_data('bricks', '')
    bricks = [b.strip() for b in bricks_str.split(",")]
    replica = get_post_data('replica', 0)
    stripe = get_post_data('stripe', 0)
    transport = get_post_data('transport', 'tcp')
    force = get_post_data('force', False)

    return volume.create(name, bricks, replica, stripe, transport, force)


@app.route("/api/<int:version>/volumes/<string:name>", methods=["DELETE"])
@requires_auth(['glusterroot'])
@api
def volume_delete(version, name):
    return volume.delete(name)


@app.route("/api/<int:version>/volumes/<string:name>/start",
           methods=["PUT"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_start(version, name):
    return volume.start(name)


@app.route("/api/<int:version>/volumes/<string:name>/start-force",
           methods=["PUT"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_start_force(version, name):
    try:
        return resp_success(volume.start(name, force=True))
    except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
        return resp_error(200, e)


@app.route("/api/<int:version>/volumes/<string:name>/stop",
           methods=["PUT"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_stop(version, name):
    try:
        return resp_success(volume.stop(name))
    except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
        return resp_error(200, e)


@app.route("/api/<int:version>/volumes/<string:name>/stop-force",
           methods=["PUT"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_stop_force(version, name):
    try:
        return resp_success(volume.stop(name, force=True))
    except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
        return resp_error(200, e)


@app.route("/api/<int:version>/volumes/<string:name>/restart",
           methods=["PUT"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_restart(version, name):
    try:
        return resp_success(volume.restart(name))
    except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
        return resp_error(200, e)


@app.route("/api/<int:version>/volumes", methods=["GET"])
@requires_auth(['glusterroot', 'glusteradmin', 'glusteruser'])
@api
def volumes_get(version):
    try:
        return resp_success(volume.info())
    except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
        return resp_error(200, e)


@app.route("/api/<int:version>/volumes/<string:name>", methods=["GET"])
@requires_auth(['glusterroot', 'glusteradmin', 'glusteruser'])
@api
def volume_get(version, name):
    try:
        return resp_success(volume.info(name))
    except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
        return resp_error(200, e)


@app.route("/api/<int:version>/peers", methods=["GET"])
@requires_auth(['glusterroot', 'glusteradmin', 'glusteruser'])
@api
def peers_get(version):
    try:
        return resp_success(peer.info())
    except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
        return resp_error(200, e)


@app.route("/api/<int:version>/peers/<string:hostname>", methods=["POST"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def peer_create(version, hostname):
    try:
        return resp_success(peer.probe(hostname))
    except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
        return resp_error(200, e)


@app.route("/api/<int:version>/peers/<string:hostname>", methods=["DELETE"])
@requires_auth(['glusterroot'])
@api
def peer_delete(version, hostname):
    try:
        return resp_success(peer.detach(hostname))
    except (volume.GlusterCliFailure, volume.GlusterCliBadXml) as e:
        return resp_error(200, e)
