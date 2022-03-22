import numpy as np

def sor(n,A,B,x0,x,eps,k,w):
    """超松弛迭代法
                Args:
                    n: 矩阵阶数
                    A:为方程组的系数矩阵
                    B:为方程组右端的列向量
                    x:为迭代初值构成的列向量
                    x:迭代向量
                    eps :精度误差
                    k:最大迭代次数
                    w:松弛因子
                Returns:
                    times:迭代次数
                    x：Array数组x的解
                Raises:
    """
    times = 1
    while times < k:
        for i in range(n):
            temp = 0
            temps = x0.copy()
            for j in range(n):
                if i != j:
                    temp += x0[j] * A[i][j]
            x[i] = w*((B[i] - temp) / A[i][i])
            x0[i] = x[i].copy()
        calTemp = max(abs(x - temps))
        times += 1
        if calTemp < eps:
            print("精确度等于", eps, "时，超松弛迭代法需要迭代", times, "次收敛")
            return (x, times)
        else:
            x0 = x.copy()
    print("在最大迭代次数内不收敛", "最大迭代次数后的结果为", x)
    return None
A = np.array([[4,-2,-1], [-2,4,-2], [-1,-2,3]])
B = np.array([0,-2,3])
x0 = np.array([1.0,1.0,1.0])
x = np.array([0,0,0])
eps = 1e-4
n = 3
k = 100
w = 1.45
sor(n,A,B,x0,x,eps,k,w)