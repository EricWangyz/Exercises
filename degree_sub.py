#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/29 20:52   
# @Author  : Eric Wang         
# @File    : degree_sub.py        

import math

m = int(input())

for i in range(m):
    degree = list(map(int, input().split(' ')))
    res = math.sin((degree[0] - degree[1]) *math.pi / 180)

    print('%.02f' % res)

