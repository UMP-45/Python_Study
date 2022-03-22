#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keras.datasets import mnist
from collections import OrderedDict
import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np

class FullyConnected:
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
     
    def backward(self, dout): #dout上游传来的倒数
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        return dx

class Relu:
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
        
    def softmax(self, x):
        if x.ndim == 2: #ndim维度
            x = x.T
            x = x - np.max(x, axis=0)
            y = np.exp(x) / np.sum(np.exp(x), axis=0)
            return y.T 

        x = x - np.max(x) # 溢出对策
        return np.exp(x) / np.sum(np.exp(x))

    def cross_entropy_error(self, y, t):
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
       
class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01): 
        # 初始化权重
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size) #rand函数根据给定维度生成[0,1)之间的数据，包含0，不包含1
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

        # 生成层
        self.layers = OrderedDict()   # 有序字典
        self.layers['FC1'] = FullyConnected(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['FC2'] = FullyConnected(self.params['W2'], self.params['b2'])
        self.lastLayer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
        return x

    # x:输入数据, t:监督数据
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastLayer.forward(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1 :
            t = np.argmax(t, axis=1)
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    # x:输入数据, t:标签数据
    def gradient(self, x, t):
        # forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.lastLayer.backward(dout)
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)

        # 设定
        grads = {}
        grads['W1'] = self.layers['FC1'].dW
        grads['b1'] = self.layers['FC1'].db
        grads['W2'] = self.layers['FC2'].dW
        grads['b2'] = self.layers['FC2'].db
        return grads
        
class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None
        
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
            
def change_one_hot_label(X):
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        row[X[idx]] = 1
        
    return T
    
def draw(title, x, y, xlabel, ylabel, label, color, *, ylim = None,linestyle = "-"): 
    plt.plot(x, y, label = label, color = color, linestyle = linestyle)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title(title)
    if ylim != None:
        plt.ylim(0, 1.0)
    plt.legend(loc='lower right')

def draw_both(title, x, y_1, y_2, xlabel, ylabel, y_1_label, y_2_label, *, line_1 = "-", line_2 = "--"):
    plt.plot(x, y_1, label = y_1_label)
    plt.plot(x, y_2, label = y_2_label, linestyle = line_2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(0, 1.0)
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.legend(loc='lower right')
    plt.title(title)
    
if __name__ == "__main__":
    (x_train, t_train), (x_test, t_test) = mnist.load_data()
    x_train = x_train.reshape(x_train.shape[0], -1) #x_train.shape[0] = 60000
    x_train = x_train.astype(np.float32) / 255.0
    x_test = x_test.reshape(x_test.shape[0], -1) #x_test.shape[0] = 10000
    x_test = x_test.astype(np.float32) / 255.0

    t_train = change_one_hot_label(t_train)
    t_test = change_one_hot_label(t_test)
    
    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)
    optimizer = AdaGrad()
    
    iters_num = 6000
    train_size = x_train.shape[0]
    batch_size = 100
    learning_rate = 0.1
    train_loss_list = []
    train_acc_list = []
    test_acc_list = []
    
    iter_per_epoch = max(train_size / batch_size, 1)

    for i in range(iters_num):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]
    
        params = network.params
        grad = network.gradient(x_batch, t_batch)
        optimizer.update(params,grad)
        
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)
    
        if i % iter_per_epoch == 0:
            train_acc = network.accuracy(x_train, t_train)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)
            print('train acc, test acc | {0:.4f}, {1:.4f}'.format(train_acc, test_acc))

    x = np.arange(len(train_acc_list))
    x_loss = np.arange(len(train_loss_list))
    
    plt.figure(1,dpi=100)
    ax1 = plt.subplot(221) #创建 nxn 的子图，第三个数字为序号
    ax2 = plt.subplot(222)
    ax3 = plt.subplot(223)
    ax4 = plt.subplot(224)
    
    plt.sca(ax1)
    draw("AdaGrad_train", x, train_acc_list, "epochs", "accuracy", "train acc", "red", ylim = 1.0)
    
    plt.sca(ax2)
    draw("AdaGrad_test", x, test_acc_list, "epochs", "accuracy", "test acc", "green", ylim = 1.0,linestyle = '--')
    
    plt.sca(ax3)
    draw_both("AdaGrad-拟合曲线", x, train_acc_list, test_acc_list, "epochs", "accuracy", "train acc", "test acc")

    plt.sca(ax4)
    draw("AdaGrad_loss", x_loss, train_loss_list, "iters", "loss", "train_loss", "green")

    plt.tight_layout() #调整每个子图间的间距
    plt.savefig("AdaGrad.jpg")
    plt.show()
    