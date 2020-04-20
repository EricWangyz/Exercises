#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/29 20:15   
# @Author  : Eric Wang         
# @File    : 多项式的值.py        

m = int(input())

for i in range(m):
    n = int(input())
    coe = list(map(int,input().split(' ')))
    x = int(input())
    sum_ = 0
    for j in range(n+1):
        sum_ += pow(x,j) * coe[j]
    print(sum_)