#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/27 10:15   
# @Author  : Eric Wang         
# @File    : 两点间距离.py        

import math

m = int(input("input the num of example:"))

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    dis_2 = (x2-x1)**2 + (y2-y1)**2
    res = math.sqrt(dis_2)
    print("%.2f" % res)

if __name__ == '__main__':
    pass