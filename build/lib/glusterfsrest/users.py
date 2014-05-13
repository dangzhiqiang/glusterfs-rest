# -*- coding: utf-8 -*-
"""
    users.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

import sqlite3
from glusterfsrest import settings
import hashlib


conn = None
cursor = None


def pwdhash(inp):
    return hashlib.md5(inp).hexdigest()


def connect():
    global conn, cursor
    conn = sqlite3.connect(settings.get("USERS_DB"))
    cursor = conn.cursor()


def install():
    create_table = """CREATE TABLE IF NOT EXISTS  glusterrestusers(
    username VARCHAR(200) PRIMARY KEY,
    password VARCHAR(200),
    restgroup VARCHAR(30) DEFAULT 'glusteruser',
    enabled INT DEFAULT 1,
    updated_at DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_table)


def reinstall():
    drop_table = "DROP TABLE IF EXISTS glusterrestusers"
    cursor.execute(drop_table)

    create_table = """CREATE TABLE glusterrestusers(
    username VARCHAR(200) PRIMARY KEY,
    password VARCHAR(200),
    restgroup VARCHAR(30) DEFAULT 'glusteruser',
    enabled INT DEFAULT 1,
    updated_at DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_table)


def useradd(username, password, group):
    query = """INSERT OR IGNORE INTO glusterrestusers(
    username, password, restgroup
    ) VALUES(?, ?, ?)
    """
    cursor.execute(query, (username, pwdhash(password), group))
    if cursor.rowcount > 0:
        conn.commit()
        return True
    else:
        return False


def usermod(username, group):
    query = """UPDATE glusterrestusers SET
    restgroup = ? WHERE username = ?
    """
    cursor.execute(query, (group, username))
    if cursor.rowcount > 0:
        conn.commit()
        return True
    else:
        return False


def userdel(username):
    query = """DELETE FROM glusterrestusers
    WHERE username = ?
    """
    cursor.execute(query, (username, ))
    if cursor.rowcount > 0:
        conn.commit()
        return True
    else:
        return False


def passwd(username, password):
    query = """UPDATE glusterrestusers SET
    password = ? WHERE username = ?
    """
    cursor.execute(query, (pwdhash(password), username))
    if cursor.rowcount > 0:
        conn.commit()
        return True
    else:
        return False


def authenticate(username, password, groups):
    query = """
    SELECT username, restgroup FROM glusterrestusers WHERE
    username = ? AND password = ?
    """
    cursor.execute(query, (username, pwdhash(password)))
    row = cursor.fetchone()

    if row is None:
        return False

    if row[1] in groups:
        return True

    return False


def get():
    users = []
    query = """
    SELECT username, restgroup FROM glusterrestusers WHERE enabled = 1
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        users.append((row[0], row[1]))
    return users
