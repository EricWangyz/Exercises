#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 16:29
# @Author  : Eric Wang
# @File    : insertion_sort.py

import random

RANGE = 100
LENGTH = 5
my_list = random.sample(range(RANGE), LENGTH)  # 在指定序列中获取指定长度的片段
print("before sort:", my_list)


def insertion_sort(list):
    """
    直接插入排序(Straight Insertion Sort)的基本思想是：把n个待排序的元素看成为一个有序表和一个无序表。
    开始时有序表中只包含1个元素，无序表中包含有n-1个元素，排序过程中每次从无序表中取出第一个元素，
    将它插入到有序表中的适当位置，使之成为新的有序表，重复n-1次可完成排序过程
    :param list:
    :return:
    """
    # 获取列表长度
    length = len(list)

    for i in range(1, length):
        j = i - 1  # 设置无序列表中当前元素的的前一个元素的标识，即有序列表的最后一个元素

        # 如果无序列表中当前元素小于前一个元素，则将当前值存入临时变量，待找到合适的位置再插入即可
        if list[i] < list[j]:
            temp = list[i]
            list[i] = list[j]  # 前一个元素后移一位

            j = j - 1  # 继续往前比较
            while j >= 0 and list[j] > temp:  # j>=0保证还在有序列表中寻找，
                list[j + 1] = list[j]  # 发现有大于临时变量的，则往后移一位
                j = j - 1

            list[j + 1] = temp  # 临时值与有序列表比较完毕，将临时值赋给合适的位置list[j]处

    return list


if __name__ == "__main__":
    insertion_sort(my_list)
    print("after sort:", my_list)



def insertion(sortList):
    for i in range(1, len(sortList)):
        x = sortList[i] # 无序列表
        for j in range(i,-1,-1): # 有序列表，i,i-1,i-2,...
            if x < sortList[j-1]: # 如果比当前索引前面的数
                sortList[j] = sortList[j-1]
            else:
                break
            sortList[j] = x
    return sortList
