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
import numpy

from foamParse import check_header
from foamParse import read_file
from foamParse import read_data
from foamVisualise import visualise

def interface(parser, args):
    assert args['opt'] == 'interface'
    point_file_string = ('%s/%s/interface/points' \
                          %(args['dir'], args['time']))
    face_file_string = ('%s/%s/interface/faces' \
                          %(args['dir'], args['time']))

    point_read = read_file(parser, args, point_file_string)
    face_read = read_file(parser, args, face_file_string)

    check_header(parser, args, point_read, data_type='vectorList')
    check_header(parser, args, face_read, data_type='labelListList')

    point = read_data(parser, args, point_read, data_type='vectorList')
    face = read_data(parser, args, face_read, data_type='lableListList')
    interface = [point, face]

    visualise(parser, args, data=interface)

# ----------------------------------------------------------------- end-of-file
