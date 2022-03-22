#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math
def func(x): return math.exp(x) + 2**x + 2*math.cos(x) - 6

a = 1;
b = 2;
s = 1e-5;
k = ((math.log(b-a)-math.log(s)) / math.log(2)) - 1;

while abs(a - b) > k:
    x = (a + b) / 2
    if func(a)*func(b) < 0:
       b = x
    else: 
        a = x

print(x)   

