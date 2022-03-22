#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#神经网络
import numpy as np

class FullyConnected: #全连接网络
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None
    
    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out
     
    def backward(self, dout): # dout上游传来的倒数
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        return dx

class Relu:  #激活函数
    def __init__(self):
        self.mask = None
    
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        return dout 

class SoftmaxWithLoss:  
    def __init__(self):
        self.loss = None # 损失
        self.y = None # softmax的输出
        self.t = None # 标签数据（one-hot vector）
        
    def softmax(self, x): # 多分类问题用 softmax 函数,二分类问题使用 sigmoid 函数
        if x.ndim == 2: # ndim维度
            x = x.T
            x = x - np.max(x, axis=0)
            y = np.exp(x) / np.sum(np.exp(x), axis=0)
            return y.T 

        x = x - np.max(x) # 溢出对策
        return np.exp(x) / np.sum(np.exp(x))

    def cross_entropy_error(self, y, t): # 交叉熵误差
        if y.ndim == 1:
            t = t.reshape(1, t.size)
            y = y.reshape(1, y.size)
            
        # 监督数据是one-hot-vector的情况下，转换为正确解标签的索引
        if t.size == y.size:
            t = t.argmax(axis=1)
             
        batch_size = y.shape[0]
        return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
            
    def forward(self, x, t):
        self.t = t
        self.y = self.softmax(x)
        self.loss = self.cross_entropy_error(self.y, self.t)
        return self.loss
    
    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
        return dx
        
def change_one_hot_label(X): # 将 MNIST 的标签数据改为 one-hot 类型
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        row[X[idx]] = 1    
    return T        
    