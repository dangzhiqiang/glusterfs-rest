# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Red Hat, Inc. <http://www.redhat.com>
# This file is part of GlusterFS.

# This file is licensed to you under your choice of the GNU Lesser
# General Public License, version 3 or any later version (LGPLv3 or
# later), or the GNU General Public License, version 2 (GPLv2), in all
# cases as published by the Free Software Foundation.
#

import xml.etree.cElementTree as etree


class GlusterCliFailure(Exception):
    pass


class GlusterCliBadXml(Exception):
    pass


ParseError = etree.ParseError if hasattr(etree, 'ParseError') else SyntaxError
