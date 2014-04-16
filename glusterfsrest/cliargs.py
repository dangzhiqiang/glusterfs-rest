# -*- coding: utf-8 -*-
"""
    cliargs.py

    :copyright: (c) 2014 by Aravinda VK
    :license: BSD, see LICENSE for more details.
"""
import argparse
from argparse import RawDescriptionHelpFormatter, ArgumentParser

PROG_DESCRIPTION = """

"""


def get():
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            description=PROG_DESCRIPTION)

    subparser = parser.add_subparsers(dest='subcommand',
                                      title='Available glusterrest commands',
                                      metavar='')

    # Sub commands
    subparser.add_parser('install', help=argparse.SUPPRESS)
    subparser.add_parser('reinstall', help=argparse.SUPPRESS)
    parser_show = subparser.add_parser(
        'show',
        help='Show info about users/groups/config'
    )
    parser_set = subparser.add_parser(
        'set',
        help='set config options'
    )
    parser_useradd = subparser.add_parser('useradd', help='Add REST user')
    parser_usermod = subparser.add_parser('usermod', help='Modify REST user')
    parser_userdel = subparser.add_parser('userdel', help='Delete REST user')
    parser_passwd = subparser.add_parser('passwd', help='Change Password')

    # Show arguments
    parser_show.add_argument('option',
                             type=str,
                             help='Show info about users/groups/config',
                             choices=['users', 'groups', 'config'])

    # Set arguments
    parser_set.add_argument('config',
                            type=str,
                            help='REST services PORT',
                            choices=['port'])
    parser_set.add_argument('value',
                            type=str,
                            help='Value to set',
                            default='9000')

    # useradd arguments
    parser_useradd.add_argument('username',
                                type=str,
                                help='USERNAME')
    parser_useradd.add_argument('-g',
                                '--group',
                                type=str,
                                help='GROUP',
                                default='glusteruser',
                                choices=['glusterroot', 'glusteradmin',
                                         'glusteruser'])
    parser_useradd.add_argument('-p',
                                '--password',
                                type=str,
                                help='PASSWORD',
                                default='')

    # usermod arguments
    parser_usermod.add_argument('username',
                                type=str,
                                help='USERNAME')
    parser_usermod.add_argument('-g',
                                '--group',
                                type=str,
                                help='GROUP',
                                default='glusteruser',
                                choices=['glusterroot', 'glusteradmin',
                                         'glusteruser'])
    parser_usermod.add_argument('-p',
                                '--password',
                                type=str,
                                help='PASSWORD')

    # userdel arguments
    parser_userdel.add_argument('username',
                                type=str,
                                help='USERNAME')

    # passwd arguments
    parser_passwd.add_argument('username',
                               type=str,
                               help='USERNAME')
    parser_passwd.add_argument('-p',
                               '--password',
                               type=str,
                               help='PASSWORD',
                               default='')

    return parser.parse_args()
