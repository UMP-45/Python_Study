#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description = 'sort the numbers')
parser.add_argument('integers', metavar='N', type=int,nargs='+')
args = parser.parse_args()

def mysort(L):
    count = 0
    for i in range(len(L)-1):
        if L[i] < L[i+1] or L[i] == L[i+1]:
           pass 
        else: L[i], L[i+1] = L[i+1],L[i]
        count += 1
    return(L,count)

print(mysort([*args.integers]))
# print(type(args.integers))
# print(sort(args.integers))

# for i in L: print(i)
# for i in range(len(L)-1): print(l[i])