#!/usr/bin/env python3
#------------------------------------------------------------------------------
# =========                 |
# \\      /  F ield         | foamTEX: Open Source CFD to laTeX
#  \\    /   O peration     | Web: https://github.com/LeoTurnell-Ritson/foamTEX
#   \\  /    A nd           | For copyright notice see file Copyright
#    \\/     M anipulation  |
#------------------------------------------------------------------------------
#
# Description
#
#
#
#------------------------------------------------------------------------------

import sys
import os
import re
import argparse
import numpy

from foamParse import check_header
from foamInterface import interface

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='In house visualisation ' \
                                     'tool for foam data files')
    parser.add_argument('-t', '--time', help='Time sub-directory', \
                        required=True)
    parser.add_argument('-o', '--opt', help='Choice of visualisation', \
                        required=True)
    parser.add_argument('-d', '--dir', help='Case Directory (defaults to ' \
                        'current)', required=False)
    args = vars(parser.parse_args())

    # If not specified set dir as to default (cwd)
    if args['dir'] == None:
        args['dir'] = os.getcwd()

    # List and description of current opts
    opt_list = ['interface']
    opt_description = ['Draw interface mesh from point and face data (in '\
                       '%s/%s/interface/.)' %(args['dir'], args['time'])]

    # Main function loop, with opt checking
    if not args['opt'] in opt_list:
        parser.print_usage()
        print(parser.prog + ': error: user supplied OPT is not in ' \
              'list of supplied operations, try:')
        for i in range(0, len(opt_list)):
            print('\t' + opt_list[i] + '\t' + \
                  opt_description[i])
        sys.exit(1)
    else:
        if args['opt'] == 'interface':
            interface(parser, args)
        else:
            print(parser.prog + ': error: implantation void')
            sys.exit(1)

# ----------------------------------------------------------------- end-of-file
