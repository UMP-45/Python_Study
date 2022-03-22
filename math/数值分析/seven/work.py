import numpy as np 
import matplotlib.pyplot as plt

def Least_squares(x,y):
  
#n次拟合曲线：y=a0+a1x+a2x^2+...+anx^n
  x_array = np.array([-3,-2,-1,0,1,2,3])
  y_array = np.array([4,2,3,0,-1,-2,-5])
  n = 2 #方程的次数（n<5）
  m = len(x_array)#方程个数
 
  A = np.ones(m).reshape((m,1))
  for i in range(n):
    A = np.hstack([A,(x_array**(i+1)).reshape((m,1))])
 
  X = np.dot(np.dot(A.T,A),np.dot(A.T,y_array.T))
  return a,b

if __name__ == '__main__':
  x = [0,5,10,15,20,25,30,35,40,45,50,55]
  y = [0,1.27,2.16,2.86,3.44,3.87,4.15,4.37,4.51,4.58,4.62,4.64]
  a,b = Least_squares(x,y)
  print("一次拟合曲线a,b参数：",a,b)
  y1 = a * x + b
  plt.figure(figsize=(10, 5), facecolor='w')
  plt.plot(x, y, 'ro', lw=2, markersize=6)
  plt.plot(x, y1, 'r-', lw=2, markersize=6)
  plt.grid(b=True, ls=':')
  plt.xlabel(u'X', fontsize=16)
  plt.ylabel(u'Y', fontsize=16)
  plt.show()
