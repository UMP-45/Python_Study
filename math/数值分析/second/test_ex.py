#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from sympy import *
import random

x = symbols("x")
func = x - (x**3 + 4 * x**2 - 10)/(3 * x**2 + 8*x)

begin = 1  #区间
end = 2
MAXSTEP = 100
step_count = 0
x0 = random.uniform(begin, end)
temp = func.subs(x, x0)

while step_count < MAXSTEP and abs(temp - x0) > 1e-10:
    x0 = temp
    temp = func.subs(x, x0)
    step_count += 1
print(x0)
print(step_count)