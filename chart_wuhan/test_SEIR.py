#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#易感-暴露-感染-恢复模型

import scipy.integrate as spi
import numpy as np
import pylab as pl
#import math

def modle_SEIR(INP,t):
    Y = np.zeros((4))
    V = INP
    Y[0] = -beta * V[0] * V[2]/N
    Y[1] = beta * V[0] * V[2]/N - V[1]/t_latent
    Y[2] = V[1]/t_latent - gamma * V[2]
    Y[3] = gamma * V[2]
    return Y

beta = 1.2 # 易感者成为感染者的概率
gamma = 0.1 # 康复率

t_start = 0.0
t_end = 60 # 研究时间
t_latent = 7 # 潜伏期
N = 1000 # 人群总数

R0 = 0 # 初始时刻有0个人康复
E0 = 0 # 初始时刻病毒潜伏者
I0 = 1 # 初始时刻有1个人感染
S0 = N - I0 - E0 - R0 # 初始时刻易感人数

INPUT = (S0, E0, I0, R0)

t_range = np.arange(t_start, t_end)
res = spi.odeint(modle_SEIR, INPUT, t_range)

print(res)

pl.plot(res[:,0], '-b', label="易感者")
pl.plot(res[:,1], '-o', label="潜伏者")
pl.plot(res[:,2], '-r', label="感染者")
pl.plot(res[:,3], '-g', label="康复者")

pl.legend(loc=0)
pl.title("SEIR模型")
pl.xlabel("时间")
pl.ylabel("模拟情况")
pl.rcParams['font.sans-serif']=['SimHei'] # 显示中文
pl.rcParams['axes.unicode_minus']=False
pl.savefig("SEIR模型.png")
pl.show()