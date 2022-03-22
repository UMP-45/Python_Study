#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    IsPrime[1] = False #1不为素数
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]

i = 100
L=eratosthenes(i)
L.sort()
print(L, type(L))
