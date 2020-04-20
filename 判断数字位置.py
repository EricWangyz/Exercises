#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/29 10:21   
# @Author  : Eric Wang         
# @File    : 判断数字位置.py        

m = int(input())
num = ['0','1','2','3','4','5','6','7','8','9']


for i in range(m):
    out = []
    temp = input()
    for j in range(len(temp)):
        if str(temp[j]) in num:
            out.append(j+1)
    print(' '.join(map(str, out)))
