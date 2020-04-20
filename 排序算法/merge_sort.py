#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/3/20 18:25   
# @Author  : Eric Wang         
# @File    : merge_sort.py        

import random

RANGE = 100
LENGTH = 7
my_list = random.sample(range(RANGE), LENGTH)  # 在指定序列中获取指定长度的片段
# print("before sort:", my_list)

def merge(list_a, list_b):
    ##list_a,list_b是待合并的两个列表,两个列表分别都是有序的，合并后才会有序
    merged_result = []
    i = j = 0
    while i < len(list_a) and j < len(list_b):
        if list_a[i] < list_b[j]:
            merged_result.append(list_a[i])
            i += 1
        else:
            merged_result.append(list_b[j])
            j += 1

    merged_result.extend(list_a[i:])
    merged_result.extend(list_b[j:])

    return merged_result

def merge_sort(list):
    '''
    将一个序列从中间位置分成两个序列，将这两个子序列进一步二分下去，直到所有子序列的长度为1为止。
    之后进行两两合并，得到最后的排序序列
    :param list:
    :return:
    '''
    if len(list) <= 1:
        return list

    middle = len(list) // 2
    left_list = merge_sort(list[:middle])
    # print('left:', left_list)
    right_list = merge_sort(list[middle:])
    # print('right:', right_list)

    return merge(left_list, right_list) #返回元组数据
    # left_list, right_list = left_list[:], right_list[:]
    # return left_list,right_list

if __name__ == '__main__':


    print(merge_sort(my_list))



# def merge(a, b):
#     c = []
#     h = j = 0
#     while j < len(a) and h < len(b):
#         if a[j] < b[h]:
#             c.append(a[j])
#             j += 1
#         else:
#             c.append(b[h])
#             h += 1
#
#     if j == len(a):
#         for i in b[h:]:
#             c.append(i)
#     else:
#         for i in a[j:]:
#             c.append(i)
#
#     return c
#
#
# def merge_sort(lists):
#     if len(lists) <= 1:
#         return lists
#     middle = len(lists)//2
#     left = merge_sort(lists[:middle])
#     right = merge_sort(lists[middle:])
#     # return left,right
#     return merge(left, right)
#
#
# if __name__ == '__main__':
#     a = [4, 7, 8, 3, 5, 9]
#     # l, r = merge_sort(a)
#     # print(l)
#     # print(r)
#     print(merge_sort(a))
