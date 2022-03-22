#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def search(seq, v, low, high) :
  while low <= high:
    mid = (low + high) // 2
    if v == seq[mid]: return mid
    elif v > seq[mid]: low = mid + 1
    else: high = mid - 1
  return None

# user input
try : # type check
  start = int(input('start: '))
  final = int(input('final: '))
  value = int(input('any: '))
except ValueError :
  print('only intger!')
  exit()

# logic check
if start == final: exit()
if final < start : start, final = final, start


#
ordered = []
for i in range(start, final) : ordered.append(i)
sorted(ordered[:], reverse=False)
result = search(ordered,value,0,len(ordered))

#output
print('index: ', result)
if result != None : print('value: ', ordered[result])
