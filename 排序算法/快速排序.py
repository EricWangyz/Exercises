#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 13:56
# @Author  : Eric Wang
# @File    : 快速排序.py


def quickSort(nums, start, end):
    """
    先从后面遍历，如果小于base，就交换，
    再从前面遍历，如果大于base，就交换
    当i，j相等时，就是base应该在的位置，将base赋值给nums[i]
    然后前半部分和后半部分进行递归
    :param nums: 待排序列表
    :param start: 起始位置
    :param end: 结束位置
    :return: 排好序的列表
    """
    if start < end:
        i, j = start, end
        base = nums[i]

        while i < j:
            while i < j and nums[j] >= base:
                j -= 1
            nums[i] = nums[j]

            while i < j and nums[i] <= base:
                i += 1
            nums[j] = nums[i]

        nums[i] = base

        print(nums)
        quickSort(nums, start, i - 1)
        quickSort(nums, j + 1, end)

    return nums

if __name__ == '__main__':
    nums = [6,5,4,3,2,1]
    print(quickSort(nums, 0, len(nums)-1))


def quicksort(nums, start, end):
    if start < end:
        i, j = start, end
        base = nums[i]

        while i < j:
            while i < j and nums[j] > base:
                j = j - 1
            nums[i] = nums[j]

            while i < j and nums[i] < base:
                i = i + 1
            nums[i] = nums[j]

        nums[i] = base
        quicksort(nums, start, i - 1)
        quicksort(nums, j + 1, end)
    return nums

