#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/7 15:00   
# @Author  : Eric Wang         
# @File    : 归并排序.py        

def merge(nums1, nums2):
    '''
    合并两个有序列表
    :param nums1:
    :param nums2:
    :return:
    '''
    merged = []

    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    return merged

def mergeSort(nums):
    '''
    归并排序，递归、合并
    :param nums:
    :return:
    '''
    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2

    left = mergeSort(nums[:middle])
    right = mergeSort(nums[middle:])

    sorted = merge(left, right)

    return sorted