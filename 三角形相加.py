#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/27 22:51   
# @Author  : Eric Wang         
# @File    : 三角形相加.py        

data_list = []

while True:
    temp = list(map(int,input().split()))
    if temp[0] == 0:
        break
    else:
        data_list.append(temp)

y = 0
x = 0
for data in data_list:
    y += data[0]
    x += data[1]

print("A(0,%d),B(0,0),C(%d,0)" % (y,x))