#!/usr/bin/env python3
# -*- coding:< UTF-8> -*-
import time
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('r', type=int)
args = parser.parse_args()
i=args.r

start = time.perf_counter() 
# i = input("please enter an integer: ")
r = list()
r.append(2)

for a in range(3,int(i)):
  b = False
  for b in r:
    if a%b == 0:
      b = False
      break
    else:
      b = True
  if b == True:
    r.append(a)
print(r)
t = (time.perf_counter() - start);
print(t)
