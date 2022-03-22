#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
n = int(input("input n: "))
y = [None]*n

#y[0] = 0.0953102  //不可用，如此写默认为float,造成误差迅速扩大
y[0] = math.log(11) - math.log(10)

print(y[0])

for i in range(n-1):
    y[i+1] = 1/(i+1) - 10 * y[i]
    print(y[i+1])
