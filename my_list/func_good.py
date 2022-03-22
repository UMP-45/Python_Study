#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# d = {a:1,b:2,c:3}
# di = {v:k for k,v in d.items()}

'''
   输入的值头字母M，返回脚的长度L
  (M+10)/2=L 
  L*2-10=M
'''
import sys

def M_to_L(a): return [a*2 - 10, (a+10)/2]

if 1 < len(sys.argv):
    i = int(sys.argv[len(sys.argv) - 1])
    print(M_to_L(i))

