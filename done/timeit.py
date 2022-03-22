#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#计算时间
import timeit

def f() :
  f=open('D:\\source_code\\py\\two.py','rb')
  read_data = f.read()
  f.closed
  # for i in range(10) : # range(0,999)
    # with open('D:\\source_code\\py\\two.py','rb') as f:
      # read_data = f.read()
    # f.closed
    # return ''

print(timeit.Timer('f()', setup="from __main__ import f").timeit())

# def test():
    # """Stupid test function"""
    # L = [i for i in range(100)]

# if __name__ == '__main__':
    # import timeit
    # print(timeit.timeit("test()", setup="from __main__ import test"))