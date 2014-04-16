# -*- coding: utf-8 -*-
"""
    utils.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

import subprocess


def execute(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, env=None, close_fds=True):
    p = subprocess.Popen(cmd,
                         stdin=stdin,
                         stdout=stdout,
                         stderr=stderr,
                         env=env,
                         close_fds=close_fds)

    (out, err) = p.communicate()
    return (p.returncode, out, err)
