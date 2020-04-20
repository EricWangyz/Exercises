#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/3/21 22:12   
# @Author  : Eric Wang         
# @File    : counting_sort.py        

import random

RANGE = 100
LENGTH = 5

my_list = random.sample(range(RANGE), LENGTH)
print('before sort:', my_list)

def counting_sort(myList):
    # 计算序列长度
    length = len(myList)
    #列表中的最大值
    max_value = max(myList)
    # 设置输出序列并初始化为0
    output_list = [0 for _ in range(length)]
    # 计数序列，初始化全为0
    count_list = [0 for _ in range(max_value + 1)]
    # 对于要排序的序列，将每个数字放置到以这个数为索引的序列中
    for j in myList:
        count_list[j] += 1
    # 计算小于等于索引数的数的个数
    for i in range(1, len(count_list)):
        count_list[i] += count_list[i-1]
    # 直接将改数放置到以小于这个数的数的个数为索引的位置上，比如，有5个数比a小，则将a放置到list[5]即可
    for j in myList:
        output_list[count_list[j] - 1] = j
        # count_list[j] -= 1

    return output_list

if __name__ == '__main__':
    output_list = counting_sort(my_list)
    print('after sort:', output_list)
