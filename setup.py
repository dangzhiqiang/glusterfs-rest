# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Red Hat, Inc. <http://www.redhat.com>
# This file is part of GlusterFS.

# This file is licensed to you under your choice of the GNU Lesser
# General Public License, version 3 or any later version (LGPLv3 or
# later), or the GNU General Public License, version 2 (GPLv2), in all
# cases as published by the Free Software Foundation.
#

from setuptools import setup


setup(
    name="GlusterFS REST API Server",
    version="0.1",
    packages=["glusterfsrest", "glusterfsrest.cli"],
    include_package_data=True,
    install_requires=['argparse', 'flask', 'gunicorn', 'pyyaml'],
    entry_points={
        "console_scripts": [
            "glusterrest = glusterfsrest.glusterrest:main",
        ]
    },
    package_data={'glusterfsrest': ['doc/*.yml', 'templates/*', 'static/*']},
    data_files=[('/usr/bin', ['bin/glusterrestd']),
                ('/var/lib/glusterd/rest/',
                 ['data/port'])],
    platforms="linux",
    zip_safe=False,
    author="Aravinda VK",
    author_email="mail@aravindavk.in",
    description="GlusterFS REST API server",
    license="BSD",
    keywords="glusterfs, cli, rest",
    url="https://github.com/aravindavk/glusterfs-rest",
)
