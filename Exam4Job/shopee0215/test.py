#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2020/2/15 13:58   
# @Author  : Eric Wang         
# @File    : test.py        


import sys

for line in sys.stdin:
    data = list(map(int,line.split(",")))
    # print(data)
    # print(data)

    data = sorted(data)
    size = len(data)

    if size % 2 == 0:
        res = (data[size//2] + data[size//2 - 1])
        # res = res / 2
        print(res / 2)
    else:
        res = data[(size - 1) // 2]
        print(res)


