#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bisect, argparse # binray search 二分查找, arguments parse 参数剖析
def msgq(num, msg) : print(msg); exit(num) # 输出信息与状态码的退出
parser = argparse.ArgumentParser() # 可设描述 can set description=''
parser.add_argument('--top', '-t', type=int, default=0, help='min intger') # 可设必须项 required=True
parser.add_argument('--end', '-e', type=int, default=0, help='max intger')
parser.add_argument('--val', '-v', type=int, default=0, help='search intger')
args = parser.parse_args(); top, end, val = args.top, args.end, args.val

if top == end == val : # arguments check
  try : # interactive begin
    top = int(input('pls interactive setting, because No arguments.\ntop:'))
    end, val = int(input('end:')), int(input('val:'))
  except ValueError : msgq(None, 'only intger!',)

if end == top : msgq(None, 'empty sequence check input.') # logic check
elif end < top : top, end = end, top # swap

seq = range(top, end) # Get Sequence
index = bisect.bisect_left(seq, val)

print('index:', index) # output block
if index != 'None' : print('value:', seq[index]) # isinstance(int, index)
