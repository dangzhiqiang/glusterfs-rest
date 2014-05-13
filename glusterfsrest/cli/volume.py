# -*- coding: utf-8 -*-
"""
    cli.volume.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

from glusterfsrest import utils
from glusterfsrest.exceptions import GlusterCliBadXml, ParseError


VOLUME_CMD = ['gluster', '--mode=script', 'volume']


def _parse_a_vol(volume_el):
    value = {
        'name': volume_el.find('name').text,
        'uuid': volume_el.find('id').text,
        'type': volume_el.find('typeStr').text.upper().replace('-', '_'),
        'status': volume_el.find('statusStr').text.upper(),
        'num_bricks': int(volume_el.find('brickCount').text),
        'distribute': int(volume_el.find('distCount').text),
        'stripe': int(volume_el.find('stripeCount').text),
        'replica': int(volume_el.find('replicaCount').text),
        'transport': volume_el.find('transport').text,
        'bricks': [],
        'options': []
    }
    print value
    if value['transport'] == '0':
        value['transport'] = 'TCP'
    elif value['transport'] == '1':
        value['transport'] = 'RDMA'
    else:
        value['transport'] = 'TCP,RDMA'

    for b in volume_el.findall('bricks/brick'):
        try:
            value['bricks'].append({"name": b.find("name").text,
                                    "hostUuid": b.find("hostUuid").text})
        except AttributeError:
            value['bricks'].append(b.text)

    for o in volume_el.findall('options/option'):
        value['options'].append({"name": o.find('name').text,
                                 "value": o.find('value').text})

    return value


def _parseinfo(volinfo):
    tree = utils.checkxmlcorrupt(volinfo)
    volumes = []
    for el in tree.findall('volInfo/volumes/volume'):
        try:
            volumes.append(_parse_a_vol(el))
        except (ParseError, AttributeError, ValueError) as e:
            raise GlusterCliBadXml(str(e))

    return volumes


def info(name=None):
    cmd = VOLUME_CMD + ["info"] + ([name] if name else [])
    return utils.execute_and_output(cmd, _parseinfo)


@utils.statuszerotrue
def start(name, force=False):
    cmd = VOLUME_CMD + ["start", name]
    if force:
        cmd += ["force"]

    return cmd


@utils.statuszerotrue
def stop(name, force=False):
    cmd = VOLUME_CMD + ["stop", name]
    if force:
        cmd += ["force"]

    return cmd


@utils.statuszerotrue
def create(name, bricks, stripe=0, replica=0, transport='tcp', force=False):
    cmd = VOLUME_CMD + ["create", name]
    if stripe > 0:
        cmd += ["stripe", stripe]

    if replica > 0:
        cmd += ["stripe", stripe]

    cmd += ["transport", transport]

    cmd += bricks

    if force:
        cmd += ["force"]

    return cmd


@utils.statuszerotrue
def delete(name, force=False):
    cmd = VOLUME_CMD + ["delete", name]
    if force:
        cmd += ["force"]

    return cmd


def restart(name):
    start(force=True)


def healinfo(name):
    pass


@utils.statuszerotrue
def addbrick(volumename, brickpath):
    pass


@utils.statuszerotrue
def removebrick(volumename, brickpath):
    pass
