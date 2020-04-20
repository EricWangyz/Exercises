#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/7 11:15   
# @Author  : Eric Wang         
# @File    : 插入排序.py        

def insertionSort(nums):
    '''
    分为有序列表和无序列表，将无序列表中小于有序列表最后一个数的数插入到有序列表中合适的位置
    :param nums:
    :return:
    '''
    length = len(nums)

    for i in range(1, length):
        j = i -1

        if nums[i] < nums[j]:
            tmp = nums[i]
            nums[i] = nums[j]
            j = j - 1

            while j >= 0 and nums[j] > tmp:
                nums[j+1] = nums[j]
                j = j - 1
            nums[j+1] = tmp

    return nums

# def insert(nums):
#     length = len(nums)
#     for i in range(1,length):
#         j = i - 1
#
#     if nums[i] < nums[j]:
#         tmp = nums[i]
#         nums[i] = nums[j]
#
#         j = j - 1
#         while j > 0 and nums[j] > tmp:
#             nums[j+1] = nums[j]
#             j = j -1
#         nums[j+1] = tmp


def insert(nums):
    length = len(nums)
    for i in range(1, length):
        j = j - 1

        if nums[i] < nums[j]:
            tmp = nums[i]
            nums[i] = nums[j]
            j = j - 1

            while j > 0 and nums[j] > tmp:
                nums[j+1] = nums[j]
                j = j - 1
            nums[j+1] = tmp

    return nums

