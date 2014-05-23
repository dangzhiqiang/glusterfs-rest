# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Red Hat, Inc. <http://www.redhat.com>
# This file is part of GlusterFS.

# This file is licensed to you under your choice of the GNU Lesser
# General Public License, version 3 or any later version (LGPLv3 or
# later), or the GNU General Public License, version 2 (GPLv2), in all
# cases as published by the Free Software Foundation.
#

from glusterfsrest import utils
from glusterfsrest.exceptions import GlusterCliBadXml, ParseError


PEER_CMD = ['gluster', '--mode=script', 'peer']
POOL_CMD = ['gluster', '--mode=script', 'pool']


def _parse_a_peer(peer_el):
    value = {
        'id': peer_el.find('uuid').text,
        'name': peer_el.find('hostname').text,
        'status': peer_el.find('connected').text
    }

    if value['status'] == '1':
        value['status'] = 'CONNECTED'
    else:
        value['status'] = 'DISCONNECTED'

    return value


def _parsepoollist(peerinfo):
    tree = utils.checkxmlcorrupt(peerinfo)
    peers = []
    for el in tree.findall('peerStatus/peer'):
        try:
            peers.append(_parse_a_peer(el))
        except (ParseError, AttributeError, ValueError) as e:
            raise GlusterCliBadXml(str(e))

    return peers


def info():
    cmd = POOL_CMD + ["list"]
    return utils.execute_and_output(cmd, _parsepoollist)


def attach(hostname):
    return utils.checkstatuszero(PEER_CMD + ["probe", hostname])


def detach(hostname, force=False):
    cmd = PEER_CMD + ["detach", hostname]
    if force:
        cmd += ["force"]

    return utils.checkstatuszero(cmd)
