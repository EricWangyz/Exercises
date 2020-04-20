#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/26 21:16   
# @Author  : Eric Wang         
# @File    : 直角三角形和周长.py

from math import sqrt

m = int(input())

for i in range(m):

    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    # print(x1, y1, x2, y2, x3, y3)
    a = (y3 - y2) ** 2 + (x3 - x2) ** 2
    b = (y3 - y1) ** 2 + (x3 - x1) ** 2
    c = (y1 - y2) ** 2 + (x1 - x2) ** 2
    middle_min = [a, b, c]
    max_d = max(a, b, c)
    middle_min.remove(max_d)

    # right angle
    sum = 0
    for i in range(len(middle_min)):
        sum += middle_min[i]
    if sum == max_d:
        print("Yes")
    else:
        print("No")

    l = sqrt(a) + sqrt(b) + sqrt(c)
    print("%.2f" % l)
