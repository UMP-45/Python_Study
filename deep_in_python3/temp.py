# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

list_n=[]
i=2
for i in range (1,100):
    j=1
    for j in range(1,i):
        if(i%j==0):
            break
    else:
        list_n.append(i)
print(list_n)
sum_n = 0
for i in range(len(list_n)):
    sum_n += list_n[i]
    print(sum_n)
    
print(sum_n)
