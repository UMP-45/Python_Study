#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pylab import mpl

class draw():
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