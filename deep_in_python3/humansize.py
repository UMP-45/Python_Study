#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

# a_kiloybyte_is_1024_bytes = True

parser = argparse.ArgumentParser(description='Convert a file size to human-readable form.')
parser.add_argument('integers', metavar='N', type=int,
                    help='an integer for the accumulator')
parser.add_argument('string')
args = parser.parse_args()
SUFFIXES = {1000:['KB','MB','GB','TB','PB','EB','ZB','YB'],
            1024:['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']}

# if args.string ==
			
def approximate_size(size,a_kiloybyte_is_1024_bytes = True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kiloybyte_is_1024_bytes -- if True (default), use multiples of 1024
                                 if False, use multiples of 1000
    Returns: string'''
    if size < 0: raise valueError('number must be non-negative')
    multiple = 1024 if a_kiloybyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /=multiple #size = size / multiple
        if size < multiple: return '{0:.1f} {1}'.format(size,suffix)
    raise ValueError('number too large') 
if __name__ == '__main__':
    print(approximate_size(args.integers,args.string))
    