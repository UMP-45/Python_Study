#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class shoes:
    name = ''
    price = 0
    size = ''
    def __init__(self,name,price,size):
        self.name = name
        self.price = price 
        self.size = size

A = shoes('A',100,'s')
B = shoes('B',200,'m')
C = shoes('C',300,'l')
a = input()
print(a)
print(A.name)

# print('',input())
# print('',A.price)

#a = A.price
#print(a)