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
import re
import numpy

def check_header(parser, args, read, format='ascii', data_type='default'):

    try:
        header = re.search(r'\{(.*?)\}', read, re.S).group(1)
    except AttributeError:
        print(parser.prog + ': error: FoamFile header not found')
        sys.exit(1)

    try:
        name = re.search(r'object(.*?);', header, re.X).group(1).strip()
    except AttributeError:
        print(parser.prog + ': error: object name not found in FoamFile header')
        sys.exit(1)

    try:
        assert (format == \
                re.search(r'format(.*?);', header, re.X).group(1).strip())
    except AssertionError:
        print(parser.prog + ': error: format in ' \
              + name + ' FoamFile is not ' + format)
        sys.exit(1)

    try:
        assert (data_type == \
                re.search(r'class(.*?);', header, re.X).group(1).strip())
    except AssertionError:
        print(parser.prog + ': error: class of data in ' \
              + name + ' FoamFile is not ' + data_type)
        sys.exit(1)

def read_file(parser, args, file_string):

    try:
        file = open(file_string, 'r')
    except FileNotFoundError:
        print(parser.prog + ': error: No such file %s' %(file_string))
        sys.exit(1)

    return file.read()

def read_data(parser, args,read, data_type='default'):

    size = numpy.uint(re.search(r'([0-9]+)\n\(', read).group(1))

    if data_type == 'lableListList':
        data = numpy.empty([size, 3], numpy.uint)
        data_tuple = re.findall(r'\(([0-9]+) ([0-9]+) ([0-9]+)\)', read)
        for i in range(0, size):
            data[i][0] = numpy.uint(data_tuple[i][0])
            data[i][1] = numpy.uint(data_tuple[i][1])
            data[i][2] = numpy.uint(data_tuple[i][2])
    elif data_type == 'vectorList':
        data = numpy.empty([size, 3], numpy.double)
        data_tuple = re.findall(r'\(([+-]?([0-9]*[.])?[0-9]+) ([+-]?([0-9]*[.])?[0-9]+) ([+-]?([0-9]*[.])?[0-9]+)\)', read)
        for i in range(0, size):
            data[i][0] = numpy.double(data_tuple[i][0])
            data[i][1] = numpy.double(data_tuple[i][2])
            data[i][2] = numpy.double(data_tuple[i][4])

    return data

# ----------------------------------------------------------------- end-of-file
