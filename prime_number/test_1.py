#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import argparse, bisect

def writer(path,plist) :
  with open(path, 'w') as f :
    for i in plist: f.write(str(i)+'\n')

def reader(path,plist) :
  with open(path) as f : 
    for line in f: list_1.append(int(line))

def check(n,mx) :
  if mx < int(n**0.5+1) : return True
  return False

def is_prime(n,plist) :
  root = int(n**0.5 + 1)
  index = bisect.bisect_right(plist,root)
  for i in range(index) :
    if n % plist[i] == 0 : return False
  return True

def expension(n,plist) :
  root = int(n**0.5+1)
  if max(plist) < root :
    for i in range(max(plist)+2,root,2) :
      if is_prime(i,plist):plist.append(i)
  return plist

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
n=args.accumulate(args.integers)

list_1 = []
path = r'/mnt/d/source_code/py/prime_number/prime.txt'
reader(path,list_1)

root = int(n**0.5+1)
if check(root,max(list_1)) :
  expension(root,list_1)
  writer(path,list_1)

index = bisect.bisect_right(list_1,root)

for i in range(index) :
  if n % list_1[i] == 0 :
    print(list_1[i])
    exit()
print(0)
   

# with open(r'/mnt/d/source_code/py/prime_number/prime.txt') as f : 
  # for line in f:
    # list_1.append(int(line))

# with open(r'/mnt/d/source_code/py/prime_number/prime.txt') as list_2:list_2.write()
# for i in list_1 : print(i, type(i))

# mx = max(list_1)
# print(mx)

# x = int(input('>>> ')) 
# r = []
# L = eratosthenes(x,
# L.sort()
# # for i in L : print(i, type(i))
# if check(x,mx) == True:
  # # with open(r'/mnt/d/source_code/py/prime_number/prime.txt', 'w') as f :
    # # for i in L: f.write(str(i)+'\n')
  # writer(path,plist)
  # for b in L:
    # if x%b == 0:
      # print("flush,not a prime number")
      # break
    # else :
      # print("flush,a prime number")
      # break
# else :
  # for i in list_1:
    # if i < x**0.5+1:
      # r.append(i)
    # else:
      # r.append(int(x**0.5+1))
      # break
  # print(r)
  # for b in r:
    # if x%b == 0:
      # print("not prime")
      # break
    # else:
      # print('prime')
      # break
# def prime(n):
'''
取得N之平方根
读入一个列表
平方根大于列表.max() 补充列表, 若非则进行定位
根据定位对 N 取模
若从未发生整出则显示 N 为质数, 发生则返回一个质因子
'''
# def eratosthenes(n):
    # IsPrime = [True] * (n + 1)
    # IsPrime[1] = False #1不为素数
    # for i in range(2, int(n ** 0.5) + 1):
        # if IsPrime[i]:
            # for j in range(i * i, n + 1, i):
                # IsPrime[j] = False
    # return [x for x in range(2, n + 1) if IsPrime[x]]
