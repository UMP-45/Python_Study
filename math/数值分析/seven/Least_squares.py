#n次拟合曲线：y=a0+a1x+a2x^2+...+anx^n

import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

def Least_squares(x,y,n):
    k = len(x_array)#方程个数 
    X = np.ones(k).reshape((k,1))
    a = [] #a[i]为x[i-1]的系数，i>1
    for i in range(n):
        X = np.hstack([X,(x**(i+1)).reshape((k,1))]) 
    if n == 1:
        a = np.dot(np.linalg.inv(np.dot(X.T,X)),np.dot(X.T,y)) #np.linalg.inv(A): 求矩阵A逆
        return a
    if n == 2:
        a = np.dot(np.linalg.inv(np.dot(X.T,X)),np.dot(X.T,y))
        return a
    if n == 3:
        a = np.dot(np.linalg.inv(np.dot(X.T,X)),np.dot(X.T,y))
        return a

def error(y_raw,y_fitting): #原始数据与拟合数据
    D = 0 #误差和
    for i in range(len(y_raw)):
        D += (y_raw[i] - y_fitting[i])**2
    return D


x_array = np.array([0,5,10,15,20,25,30,35,40,45,50,55]) #离散数据
y_array = np.array([0,1.27,2.16,2.86,3.44,3.87,4.15,4.37,4.51,4.58,4.62,4.64])

n = 1
a1 = Least_squares(x_array,y_array,n) #a[i]为x[i-1]的系数，i>1
y1 = np.zeros(len(x_array))
for i in range(len(x_array)):
  y1[i] = a1[0] + a1[1]*x_array[i]
D1 = error(y_array,y1) #一次拟合的误差和

n = 2 
a2 = Least_squares(x_array,y_array,n)
y2 = np.zeros(len(x_array))
for i in range(len(x_array)):
  y2[i] = a2[0] + a2[1]*x_array[i] + a2[2]*(x_array[i]**2)
D2 = error(y_array,y2) #二次拟合的误差和

n = 3
a3 = Least_squares(x_array,y_array,n)
y3 = np.zeros(len(x_array))
for i in range(len(x_array)):
  y3[i] = a3[0] + a3[1]*x_array[i] + a3[2]*(x_array[i]**2) + a3[3]*(x_array[i]**3)
D3 = error(y_array,y3) #三次拟合的误差和

print("一次拟合的系数：",a1)
print("一次拟合的误差和：",D1)
print("二次拟合的系数：",a2)
print("二次拟合的误差和：",D2)
print("三次拟合的系数：",a3)
print("三次拟合的误差和：",D3)

plt.figure(1,dpi=100)
ax1 = plt.subplot(221) 
ax2 = plt.subplot(222)
ax3 = plt.subplot(223) 
ax4 = plt.subplot(224)

mpl.rcParams['font.sans-serif'] = ['SimHei'] #是图片中的文字正常输出
mpl.rcParams['axes.unicode_minus'] = False

plt.sca(ax1)
plt.scatter(x_array, y_array, color="red")
plt.plot(x_array,y1, color="green", linewidth=2)
plt.title("一次拟合")

plt.sca(ax2)
plt.scatter(x_array, y_array, color="red")
plt.plot(x_array,y2,color="black",linewidth=2)
plt.title("二次拟合")

plt.sca(ax3)
plt.scatter(x_array, y_array, color="red")
plt.plot(x_array,y3,color="blue",linewidth=2)
plt.title("三次拟合")

plt.sca(ax4)
x = [1,2,3]
D = [D1, D2, D3]
name_list = ["一次拟合", "二次拟合", "三次拟合"]
plt.bar(range(len(D)), D, tick_label=name_list)
plt.title("三种拟合的误差")

plt.tight_layout() #调整每个子图间的间距
plt.show()
