#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description = 'sort the numbers')
parser.add_argument('integers', metavar='N', type=int,nargs='+')
args = parser.parse_args()


def quick_sort(data):    
    """快速排序"""    
    if len(data) >= 2:  # 递归入口及出口        
        mid = data[len(data)//2]  # 选取基准值，也可以选取第一个或最后一个元素        
        left, right = [], []  # 定义基准值左右两侧的列表        
        data.remove(mid)  # 从原始数组中移除基准值        
        for num in data:            
            if num >= mid:                
                right.append(num)            
            else:                
                left.append(num)        
        return quick_sort(left) + [mid] + quick_sort(right)    
    else:        
        return data

array = args.integers
print(quick_sort(array))