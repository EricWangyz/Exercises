#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2020/2/15 14:40   
# @Author  : Eric Wang         
# @File    : ttttt.py        

import sys

# data = [1, 3, 5, 23, 67, 135, 456]

for line in sys.stdin:
    size = len(line)
    print(type(line))
    line = line[1:size-2]
    print(line)

    data = list(map(int,line.split(", ")))
    #
    print(data)
