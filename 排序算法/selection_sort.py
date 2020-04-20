#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 17:55
# @Author  : Eric Wang
# @File    : selection_sort.py

import random

RANGE = 100
LENGTH = 5
my_list = random.sample(range(RANGE), LENGTH)  # 在指定序列中获取指定长度的片段
print("before sort:", my_list)


def selection_sort(list):
    """
    选一个数作为基准，然后将剩下的依次与之比较，大于基准数的跳过，小于基准数的，与之交换，作为新的基准数，可得最小的数
    之后再次选定基准数，可得次小的数，
    依次类推...
    :param list:
    :return:
    """
    for i in range(0, len(list) - 1):
        smallest_index = i  # 设置当前为最小
        for j in range(i + 1, len(list)):  # 与剩下的依次作比较
            if list[smallest_index] > list[j]:  # 若出现比基准数小的，
                smallest_index = j  # 将基准标识交给这个数
        list[i], list[smallest_index] = list[smallest_index], list[i]
        # 找到最小的数之后，将其放到第i处，
        # 随着i的增加，可得最终的排序
    return list


if __name__ == "__main__":
    selection_sort(my_list)
    print(my_list)


def selection(sortList):
    for i in range(len(sortList) - 1):
        smallest_index = i  # 暂且将当前循环的第一个作为最小的
        for j in range(i + 1, len(sortList)):
            if sortList[smallest_index] > sortList[j]:
                smallest_index = j
        sortList[i], sortList[smallest_index] = sortList(smallest_index), sortList[i]
    return sortList
