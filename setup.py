# -*- coding: utf-8 -*-
"""
    setup.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

from setuptools import setup


setup(
    name="GlusterFS REST API Server",
    version="0.1",
    packages=["glusterfsrest"],
    include_package_data=True,
    install_requires=['argparse', 'flask', 'gunicorn'],
    entry_points={
        "console_scripts": [
            "glusterrest = glusterfsrest.glusterrest:main",
        ]
    },
    data_files=[('/usr/local/bin', ['bin/glusterrestd']),
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
