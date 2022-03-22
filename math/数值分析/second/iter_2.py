#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math
import random
from sympy import *

def f(x): return x**3 + 4*(x**2) -10
def g1(x) : (10/x - 4*x)**0.5

begin = 1
end = 2
N = 100
step_count = 0
x0 = random.uniform(begin,end)
temp = g1(x0)

while step_count < N and abs(temp - x0) > 1e-6:
    x0 = temp  
    temp = g1(x0)
    step_count += 1

if step_count == N:
    print("不收敛")

print(x0)
print(step_count)
