#!/usr/bin/env python3
# -*- coding:< UTF-8> -*-

# import sys
# for i in sys.argv : print(i)

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
                    # const=sum, default=max,
                    # help='sum the integers (default: find the max)')
args = parser.parse_args()
# print(args.accumulate(args.integers))
print(type(args.integers))
print(args)

