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

import numpy
import sys
import matplotlib.pyplot

from mpl_toolkits import mplot3d

def visualise(parser, args, data=None):

    if args['opt'] == 'interface':
        try:
            assert len(data) == 2
            assert data[0].dtype == numpy.double
            assert data[1].dtype == numpy.uint
        except AssertionError:
            print(parser.prog + ': error: incorrect data '\
                  'for interface visualisation')
            sys.exit(1)

# ----------------------------------------------------------------- end-of-file
