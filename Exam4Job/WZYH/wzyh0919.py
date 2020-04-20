#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/19 15:59   
# @Author  : Eric Wang         
# @File    : wzyh0919.py        

n = int(input())
if n <= 5000:

    s = 1
    for i in range(2, n+1):
        s *= i
        while s % 10 == 0:
            s /=10
        s %= 100000

    print(s%10)
else:
    pass




n = int(input())

s = 1
while n > 1:
    s *= n
    n -= 1

res = str(s)

for i in res[::-1]:
    if i != "0":
        print(i)