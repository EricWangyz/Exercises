#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/29 20:10   
# @Author  : Eric Wang         
# @File    : SF0829_最长子序列.py

N = input()
N = int(N)
data = list(map(int, input().split()))

len_list = []

for i in range(N):
    data_i = data[i:N]
    print(data_i)
    res = [data_i[0]]
    slow = 0
    fast = 1

    for j in range(len(data_i) - 1):
        if data_i[fast] >= data_i[slow]:
            res.append(data_i[fast])
            slow = fast
            fast += 1
        else:
            fast += 1
    print(res)
    print(len(res))
    len_list.append(len(res))
print(len_list)
print(max(len_list))
