#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
from sympy import *

def f(x): 
  return x**3 + 4*(x**2) -10
x = symbols("x")
def g1(x) : return x - x**3 - 4 * (x**2) + 10
def g2(x) : return (10/x - 4*x)**0.5
def g3(x) : return 0.5 * (10 - x**3)**0.5
def g4(x) : return (10/(4 + x))**0.5
def g5(x) : return x - (x**3 + 4 * x**2 - 10)/(3 * x**2 + 8*x)

list = [g1(x),g2(x),g3(x),g4(x),g5(x)]

N = 100
step_count = 0
begin = 1
end = 2

for i in list:
  print(i)
  x0 = random.uniform(begin,end)
  temp = x0
  while (step_count < N) and (abs(temp - x0) > 1e-5):
    x0 = temp
    temp = i(x0)
    step_count += 1
  if step_count == N:
    print("不收敛")
  print("求得的根为: ",x0)
  print("迭代次数: ",step_count)
  print("将所求的根带回原方程: ",f(x0))
  print("\n")

