#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/29 10:44   
# @Author  : Eric Wang         
# @File    : 复数相加.py        

m = int(input())

for i in range(m):
    temp = list(map(int, input().split(' ')))
    re = temp[0] + temp[2]
    xu = temp[1] + temp[3]
    if xu < 0:
        print('%d%di' % (re, xu))
    else:
        print('%d+%di'% (re, xu))