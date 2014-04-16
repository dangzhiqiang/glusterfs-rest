# -*- coding: utf-8 -*-
"""
    cli.peer.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

from glusterfsrest import utils
import xml.etree.cElementTree as etree


PEER_CMD = ['gluster', '--mode=script', 'peer']
POOL_CMD = ['gluster', '--mode=script', 'pool']
ParseError = etree.ParseError if hasattr(etree, 'ParseError') else SyntaxError


# def _parsepoollist():
#     """
#     <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
#     <cliOutput>
#       <opRet>0</opRet>
#       <opErrno>0</opErrno>
#       <opErrstr/>
#       <peerStatus>
#         <peer>
#           <uuid>ecbd85b7-ff89-4955-81ff-1872a577ecc2</uuid>
#           <hostname>localhost</hostname>
#           <connected>1</connected>
#         </peer>
#       </peerStatus>
#     </cliOutput>
#     """
#     pass


# def info():
#     cmd = POOL_CMD + ["list"]
#     return utils.execute_and_output(cmd, _parsepoollist)


# @utils.statuszerotrue
# def attach(hostname):
#     return PEER_CMD + ["probe", hostname]


# @utils.statuszerotrue
# def detach(hostname):
#     return PEER_CMD + ["detach", hostname]
