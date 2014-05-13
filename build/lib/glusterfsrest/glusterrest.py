# -*- coding: utf-8 -*-
"""
    glusterrest.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""

import getpass
import sys
from glusterfsrest import cliargs, users, settings


def show_users():
    usersdata = users.get()
    sys.stdout.write("%20s %10s\n" % ("User", "Group"))
    for u in usersdata:
        sys.stdout.write("%20s %10s\n" % (u[0], u[1]))


def show_config():
    sys.stdout.write("%10s %10s\n" % ("Config", "Value"))
    sys.stdout.write("%10s %10s\n" % ("Port", settings.get("PORT")))


def show_groups():
    sys.stdout.write("Available Groups:\n----------------\n")
    for g in settings.get("GROUPS").split(","):
        sys.stdout.write("%s\n" % g)


def set_port(value):
    settings.set('port', value)
    sys.stdout.write("Port updated successfully, "
                     "Restart glusterrestd to use the latest port")
    return 0


def useradd(username, password, groupname):
    return users.useradd(username, password, groupname)


def usermod(username, groupname):
    return users.usermod(username, groupname)


def userdel(username):
    return users.userdel(username)


def passwd(username, password):
    return users.passwd(username, password)


def get_password():
    passwd = getpass.getpass('Password: ')
    confirm_passwd = getpass.getpass('Confirm Password: ')
    if passwd != confirm_passwd:
        sys.stderr.write("Password didn't match\n")
        sys.exit(1)

    if passwd == '':
        sys.stderr.write("Invalid password\n")
        sys.exit(1)

    return passwd


def main():
    args = cliargs.get()
    users.connect()
    ret = 0
    if args.subcommand == 'install':
        ret = users.install()
    elif args.subcommand == 'reinstall':
        ret = users.reinstall()
    elif args.subcommand == 'show':
        ret = globals()["show_%s" % args.option]()
    elif args.subcommand == 'port':
        ret = set_port(args.port)
    elif args.subcommand == 'useradd':
        if args.password == '':
            args.password = get_password()
        ret = useradd(args.username, args.password, args.group)
    elif args.subcommand == 'usermod':
        ret = usermod(args.username, args.group)
    elif args.subcommand == 'userdel':
        ret = userdel(args.username)
    elif args.subcommand == 'passwd':
        if args.password == '':
            args.password = get_password()
        ret = usermod(args.username, args.password)

    sys.exit(0 if ret else 1)


if __name__ == '__main__':
    main()
