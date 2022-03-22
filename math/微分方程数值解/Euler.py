#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np

h = 0.5
x0 = 0
y0 = 0

def f(x): # 原方程的一阶导函数
    return float(pow(math.e,x**2))

# def y_p(x,y,h):
    # return y + h*f(x)

def y_out(y,x1,x2,h):
    return y + h/2*(f(x1)+f(x2))

Y = [0]
X = np.arange(0,3,0.5)

for i in range(5): # x的取值
    print(Y[i],  X[i])
    Y.append(y_out(Y[i],X[i],X[i+1],h))     

print(X)
print(Y)








