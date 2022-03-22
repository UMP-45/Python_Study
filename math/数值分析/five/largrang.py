import matplotlib.pyplot as plt
from pylab import mpl

x = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9] #离散数据
y = [-0.916291, -0.693147, -0.5210826, -0.357765, -0.223144, -0.105361]
 
def Lagrange(data_x,data_y,size):
    parameters=[] #参数
    i=0; #i用来控制参数的个数
    while i < size: #j用来控制循环的变量做累乘
        j = 0;
        temp = 1;
        while j < size:
            if(i != j):
                temp*=data_x[i]-data_x[j]
            j+=1;
        parameters.append(data_y[i]/temp)
        i += 1;
    return parameters
    
def Calculate(data_x,parameters,x):
    returnValue = 0
    i = 0
    n = len(parameters)
    while i < n:
        temp = 1
        j = 0;
        while j< n:
            if(i!=j):
                temp *=x-data_x[j]
            j+=1
        returnValue += temp * parameters[i]
        i += 1
    return returnValue

def Draw(data_x, data_y, label, title, color, choose):
    if choose == "plot": #画线
        plt.plot(data_x, data_y, label = label, color = color)  
    elif choose == "scatter": #画点
        plt.scatter(data_x, data_y, label = label, color = color)
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title(title)
    plt.legend(loc="upper left")

        
parameters = Lagrange(x,y,len(x))
x_copy = x.copy()
y_copy = y.copy()
x_copy.append(0.54)
x_copy.sort()
y_copy.append(Calculate(x,parameters,0.54))
y_copy.sort()

plt.figure(1,dpi=100)
ax1 = plt.subplot(221) #创建2x2的子图，第三个数字为序号
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)

plt.sca(ax1)
Draw(x, y, "离散数据", "拉格朗日插值离散数据", "red", "plot") 

plt.sca(ax2)
Draw(x_copy, y_copy, "拟合数据", "拉格朗日插值拟合数据", "green", "plot")

plt.sca(ax3)
Draw(x, y, "离散数据", "拉格朗日插值离散数据", "red", "scatter") 

plt.sca(ax4)
Draw(x_copy, y_copy, "拟合数据", "拉格朗日插值拟合数据", "green", "scatter")

plt.tight_layout() #调整每个子图间的间距
plt.show()

