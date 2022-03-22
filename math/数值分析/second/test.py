#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from sympy import *
import random

def f(x): 
  return x**3 + 4*(x**2) -10

x = symbols("x")
g1 = x - (x**3 + 4 * x**2 - 10)/(3 * x**2 + 8*x)

begin = 1  #区间
end = 2
MAXSTEP = 100
step_count = 0
x0 = random.uniform(begin, end)
temp = g1.subs(x, x0)

while step_count < MAXSTEP and abs(temp - x0) > 1e-6:
    x0 = temp
    temp = g1.subs(x, x0)
    step_count += 1

if(step_count == N):
  print("不收敛")
print("求得的根为: ",x0)
print("迭代次数: ",step_count)
print("将所求的根带回原方程: ",f(x0))
print("\n")