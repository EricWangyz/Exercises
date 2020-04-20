#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/7 15:50   
# @Author  : Eric Wang         
# @File    : 列表中偶下标降序排序奇下标不变.py        

import random


def main():
    """
    编写程序，生成一个包含20个随机整数的列表，
    然后对其中偶数下标的元素进行降序排列，奇数下标的元素不变
    :return
    """
    start_list = list()
    for i in range(10):
        start_list.append(random.randint(0, 100))
    print('start_list:', start_list)

    part_list = start_list[::2]
    print('part_list:', part_list)

    part_list.sort(reverse=True)
    print('sorted_part_list:', part_list)

    # 1
    for i in range(5):
        if i % 2 == 0:
            start_list[int(i * 2)] = part_list[i]
        else:
            pass

    # 2
    # start_list[::2] = part_list[::]

    #3
    # i = 0
    # for j in range(0,20,2):
    #     start_list[j] = part_list[i]
    #     i += 1


    print('result:', start_list)


if __name__ == '__main__':
    main()

###一个错误用法
# list1 = []
# list2 = list1.sort()

# .sort()没有返回值，不能使用复制语句