#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 13:31
# @Author  : Eric Wang
# @File    : 选择排序.py

# def selection(nums):
#     '''
#     选择排序
#     暂定当前为最小，然后在剩下的里面找最小，找到之后进行交换
#     :param nums:
#     :return:
#     '''
#     for i in range(0, len(nums)-1):
#         min_index = i
#         for j in range(i + 1, len(nums)): # 找最小
#             if nums[min_index] > nums[j]:
#                 min_index = j
#         nums[min_index],nums[i] = nums[i], nums[min_index]
#
#     return nums
#

# def selection(nums):
#     for i in range(len(nums)-1):
#         index = i
#         for j in range(i+1, len(nums)):
#             if nums[index] > nums[j]:
#                 index = j
#         nums[i], nums[index] = nums[index], nums[i]
#
#     return nums

def selection(nums):
    for i in range(len(nums)-1):
        index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[index]:
                index = j
        nums[i],nums[index] = nums[index],nums[i]

    return nums


def select(nums):
    for i in range(len(nums)-1):
        index = i
        for j in range(1,len(nums)):
            if nums[j] < nums[index]:
                index = j
        nums[i],nums[index] = nums[index],nums[i]

    return nums
