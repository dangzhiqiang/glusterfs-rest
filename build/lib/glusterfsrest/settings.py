# -*- coding: utf-8 -*-
"""
    settings.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""
import ConfigParser

CONF_FILE = '/var/lib/glusterd/rest/glusterrest.conf'
SECTION = 'settings'
config = ConfigParser.RawConfigParser()
config.read(CONF_FILE)


def get(key):
    return config.get(SECTION, key)


def set(key, value):
    config.set(SECTION, key, value)

    with open(CONF_FILE, 'wb') as configfile:
        config.write(configfile)
