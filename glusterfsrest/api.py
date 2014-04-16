# -*- coding: utf-8 -*-
"""
    api.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

from functools import wraps
from flask import Response
from glusterfsrest.restapp import app, requires_auth, resp_success, resp_error
from glusterfsrest.cli import volume, peer


apilist = []


def volume_action(name, action):
    try:
        getattr(volume, action)(name)
        return resp_success('Success')
    except volume.GlusterCliFailure as e:
        return resp_error(200, e)


def api(func):
    global apilist

    @wraps(func)
    def decorated(*args, **kwargs):
        apilist.append(func)
        return func(*args, **kwargs)

    return decorated


@app.route("/api/<int:version>/volumes", methods=["PUT"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_create(version):
    """
    url: volumes
    method: POST
    params:
        - name: bricks
          type: string
          required: true
          desc: Comma seperated Brick paths

        - name: replica
          type: int
          required: false
          desc: Replica Count
    example: >
      Hello world
    response: JSON
    """
    return Response("CREATE VOls", 200)


@app.route("/api/<int:version>/volumes", methods=["DELETE"])
@requires_auth(['glusterroot'])
@api
def volume_delete(version):
    return Response("DEL VOls", 200)


@app.route("/api/<int:version>/volumes/<string:name>/start",
           methods=["POST"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_start(version, name, action):
    return volume_action(name, 'start')


@app.route("/api/<int:version>/volumes/<string:name>/stop",
           methods=["POST"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_stop(version, name, action):
    return volume_action(name, 'stop')


@app.route("/api/<int:version>/volumes/<string:name>/restart",
           methods=["POST"])
@requires_auth(['glusterroot', 'glusteradmin'])
@api
def volume_restart(version, name, action):
    return volume_action(name, 'restart')


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
