#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#讲义71页，例5.1.1.     

import numpy as np
    
class Iterative_method:
   def __init__(self,n,A,b,x0,x,tol,k):
       self.n = n #矩阵阶数
       self.A = A #为方程组的系数矩阵
       self.b = b #为方程组右端的列向量
       self.x0 = x0 #为迭代初值构成的列向量
       self.x = x #迭代向量
       self.tol = tol #精度误差
       self.k = k #最大迭代次数

   def Jacobi(self):
       x0 = self.x0.copy()  #传拷贝，防止修改初始值
       x = self.x.copy()        
       times = 0
       
       while times < k:
           for i in range(n):
               temp = 0
               for j in range(n):
                   if i != j:
                       temp += x0[j] * A[i][j]
               x[i] = ((b[i] - temp) / A[i][i])
           eps =  max(abs(x - x0))
           times += 1
           if eps < tol:
               print("雅可比迭代法")
               print("绝对误差限：", tol)
               print("实际误差：", eps)
               print("雅可比迭代法需要迭代次数：", times)
               print("解为：", x)
               print("\n")
               return 0
           else: x0 = x.copy()
           
       print("在最大迭代次数内不收敛；\n","最大迭代次数后的结果为",x)
       print("\n")
       return 0   
     
   def Guass_seid(self):
       x0 = self.x0.copy()
       x = self.x.copy()
       times = 0  
       
       while times < k:
           temps = x0.copy()
           for i in range(n):
               temp = 0
               for j in range(n):
                   if i != j:
                       temp += x0[j] * A[i][j]
               x[i] = (b[i] - temp) / A[i][i]
               x0[i] = x[i].copy()
           eps = max(abs(x - temps))
           times += 1
           if eps < tol:
               print("高斯—塞德尔迭代法")       
               print("绝对误差限：", tol)
               print("实际误差：", eps)
               print("高斯—塞德尔迭代法需要迭代次数：", times)
               print("解为：", x)
               print("\n")
               return 0  
           else: x0 = x.copy()   
           
       print("在最大迭代次数内不收敛；\n","最大迭代次数后的结果为",x)
       print("\n")
       return 0                 
               
   def sor(self): 
       x0 = self.x0.copy()
       x = self.x.copy()
       times = 0
       w = 1.3; #松弛因子
       
       while times < k:
           temps = x0.copy()
           for i in range(n):
               temp = 0
               for j in range(n):
                   if i != j:
                       temp += x0[j] * A[i][j]
               x[i] = ((b[i] - temp) / A[i][i])
               x0[i] = x[i].copy()
           x = w * x + (1 - w) * temps   
           eps = max(abs(x - temps))
           times += 1
           if eps < tol:
               print("超松弛迭代法")      
               print("绝对误差限：", tol)
               print("实际误差：", eps)
               print("超松弛迭代法需要迭代次数：", times)
               print("解为：", x)
               print("\n")
               return 0    
           else: x0 = x.copy()  
           
       print("在最大迭代次数内不收敛；\n","最大迭代次数后的结果为",x)
       print("\n")
       return 0     
        
        
        
        
if __name__ == "__main__":
    A = np.array([[4,3,0], [3,4,-1], [0,-1,4]])
    b = np.array([24,30,-24])
    x0 = np.array([1.0,1.0,1.0])
    x = np.array([1.0,1.0,1.0])
    tol = 1e-7
    n = 3
    k = 200
    
    temp = Iterative_method(n,A,b,x0,x,tol,k)
    temp.Jacobi()
    temp.Guass_seid()
    temp.sor()