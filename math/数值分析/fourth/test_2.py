#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

class Iterative_method:
    def __init__(self,n,A,B,x0,x,eps,k):
        self.n = n; #矩阵阶数
        self.A = A; #为方程组的系数矩阵
        self.B = B; #为方程组右端的列向量
        self.x0 = x0; #为迭代初值构成的列向量
        self.x = x; #迭代向量
        self.eps = eps; #精度误差
        self.k = k; #最大迭代次数

    def Jacobi(self):
        times = 0
        while times<k:
            for i in range(n):
                temp = 0
                for j in range(n):
                    if i != j:
                        temp += x0[j] * A[i][j]
                x[i] = ((B[i] - temp) / A[i][i])
            error = max(abs(x - x0))
            times += 1
            if error < eps:
                print("精确度等于", eps, "时，雅可比迭代法需要迭代", times, "次收敛")
                print(x)
                return (x, times)
            else:
                x0 = x.copy()
        print("在最大迭代次数内不收敛","最大迭代次数后的结果为",x)
        return None
        
if __name__ == "__main__":
    A = np.array([[8,-3,2], [4,11,-1], [6,3,12]])
    b = np.array([20,33,36])
    x0 = np.array([0,0,0])
    x = np.array([0,0,0])
    tol = 1e-6
    n = 3
    k = 100
    temp = Iterative_method(n,A,b,x0,x,tol,k)
    Jacobi()