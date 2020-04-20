#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2020/2/15 15:07   
# @Author  : Eric Wang         
# @File    : sort.py        

import sys

data = [1, 3, 5, 23, 67, 135, 456]

# for line in sys.stdin:
    # data = list(map(int,line.split(",")))
    # print(data)
    # print(data)

print(data)
data.sort(reverse=True)
print(data)

# data_str = str(data)
res = []
size_list = []
data_str = []
for i in data:
    data_str.append(str(i))
    # size_list.append(len())

for j in data_str:
    size_list.append(len(j))

size_list.sort(reverse=True)
# set(size_list)
# size = len(str(data[0]))
# print(size)

for k in sorted(set(size_list),reverse=True):
    tmp = []
    for i in data:
        if len(str(i)) == k:
            tmp.append(i)
        # else:
        #     pass
    tmp.sort()
    # print(tmp)

    res = res + tmp

print(res)