#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math

def f(x,y): # 待求解微分方程
    return -y

def y_true(x): # 原方程的准确解
    return math.exp(-x)

y0 = 1 # 初值
a = 0 # 区间左端点
b = 1 # 区间右端点
h = [0.1,0.01,0.001,0.0001]# 步长
Y1 = [y0] # 近似结果
Y2 = [] # 准确结果
err = [] # 误差
# 显示Euler格式(向前欧拉公式)
def Euler_method(x_n,y_n,h):
    return y_n + h*f(x_n,y_n)

# 隐式Euler格式(向后欧拉公式)
def Euler_method_backward(x_n,y_n,y_m,h): # m=n-1
    return y_m + h*f(x_n,y_n)

# 改进的Euler格式(向前欧拉公式与梯形公式)
def Euler_method_improved(x_n,y_n,x_o,h): # o=n+1
    y_o = y_n + h*f(x_n,y_n)
    y_o = y_n +h/2*(f(x_n,y_n) + f(x_o,y_o))
    return y_o

for i in range(1):
    X = np.arange(a,b,h[3])
    h = h[3]
    for x in X:
        x = float(format(x, ".4f"))
        Y1.append(Euler_method(x,Y1[-1],h))
        Y2.append(y_true(x))

ax1 = plt.subplot(121) 
ax2 = plt.subplot(122)
plt.sca(ax1)
plt.plot(X,Y1[:-1],color="blue",linewidth=2)
plt.title("近似解")

plt.sca(ax2)
plt.plot(X,Y2,color="red",linewidth=2)    
plt.title("准确解")
plt.show()

for i in range(len(X)):
    err.append(Y2[i]-Y1[i])
    #print(X[i] , Y1[i], Y2[i])

# plt.plot(X,err)
# plt.show()