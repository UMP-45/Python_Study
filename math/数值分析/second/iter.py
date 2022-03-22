#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
from sympy import *
import math
def f(x): 
  return x**3 + 4*(x**2) -10
x = symbols("x")
g1 = x - x**3 - 4 * (x**2) + 10
g2 = (10/x - 4*x)**0.5
g3 = 0.5 * (10 - x**3)**0.5
g4 = (10/(4 + x))**0.5
g5 = x - (x**3 + 4 * x**2 - 10)/(3 * x**2 + 8*x)

list = [g2]
N = 100

for i in list:
  step_count = 0
  print(i)
  begin = 1
  end = 2
  x0 = random.uniform(begin,end)
  temp = i.subs(x,x0) #初始函数值
  print('{} {}'.format(temp, x0))
  while  (step_count < N) and (abs(temp - x0) > 1e-5):
    x0 = temp
    print('{} {}'.format(step_count, x0))
    temp = i.subs(x, x0)
    step_count += 1
  if step_count == N:
    print("不收敛")
  print("求得的根为: ",x0)
  print("迭代次数: ",step_count)
  print("将所求的根带回原方程: ",f(x0))
  print("\n")

