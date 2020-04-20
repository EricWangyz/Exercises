#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/27 10:21   
# @Author  : Eric Wang         
# @File    : 落球总路程.py        

m = int(input())
for i in range(m):
    temp = list(map(int,input().strip().split()))
    path = temp[0]
    for j in range(temp[1]-1):
        path += temp[0]/(2**j)
    print("%.2f" % path)
