#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/24 14:49   
# @Author  : Eric Wang         
# @File    : 2017集合.py


count = 0
while count < 5:

    m, n = map(int, input().split())
    list1 = [int(x) for x in input().split()]
    list2 = [int(y) for y in input().split()]

    for i in list2:
        list1.append(i)

    res_list = list(set(list1))
    # print(res_list)
    res_list.sort()
    print(" ".join(str(s) for s in res_list))
    count += 1