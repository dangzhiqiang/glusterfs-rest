# -*- coding: utf-8 -*-
"""
    cli.volume.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

from glusterfsrest import utils
import xml.etree.cElementTree as etree


VOLUME_CMD = ['gluster', '--mode=script', 'volume']
ParseError = etree.ParseError if hasattr(etree, 'ParseError') else SyntaxError


class GlusterCliFailure(Exception):
    pass


class GlusterCliBadXml(Exception):
    pass


def _checkxmlcorrupt(xmldata):
    try:
        return etree.fromstring(xmldata)
    except (ParseError, AttributeError, ValueError) as e:
        raise GlusterCliBadXml(str(e))


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
    tree = _checkxmlcorrupt(volinfo)
    volumes = []
    for el in tree.findall('volInfo/volumes/volume'):
        try:
            volumes.append(_parse_a_vol(el))
        except (ParseError, AttributeError, ValueError) as e:
            raise GlusterCliBadXml(str(e))

    return volumes


def statuszerotrue(func):
    def wrapper(*args, **kwargs):
        cmd = func(*args, **kwargs)
        rc, _, err = utils.execute(cmd + ['--xml'])
        if rc == 0:
            return True

        return GlusterCliFailure(err)

    return wrapper


def execute_and_output(cmd, func):
    rc, out, err = utils.execute(cmd + ['--xml'])
    if rc == 0:
        return func(out)

    return GlusterCliFailure(rc, err)


def info(name=None):
    cmd = VOLUME_CMD + ["info"] + ([name] if name else [])
    return execute_and_output(cmd, _parseinfo)


@statuszerotrue
def start(name):
    return VOLUME_CMD + ["start", name]


@statuszerotrue
def stop(name, force=False):
    return VOLUME_CMD + ["stop", name]


@statuszerotrue
def create(name):
    return VOLUME_CMD + ["create", name]


@statuszerotrue
def delete(name, force):
    return VOLUME_CMD + ["delete", name]


def restart(name):
    stop(force=True)
    start()


# def optget(volumename, opt=None):
#     cmd = VOLUME_CMD + ["info"] + [name] if name else []
#     return execute_and_output(cmd, _parseopt)


# @statuszerotrue
# def optset(volumename, opt, value):
#     pass


def healinfo(name):
    pass


@statuszerotrue
def addbrick(volumename, brickpath):
    pass


@statuszerotrue
def removebrick(volumename, brickpath):
    pass
