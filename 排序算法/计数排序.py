#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/7 14:10   
# @Author  : Eric Wang         
# @File    : 计数排序.py        

def countSort(nums):
    length = len(nums)
    max_num = max(nums)
    res = [0 for _ in range(length)]
    counter = [0 for _ in range(max_num + 1)]

    for i in nums:
        counter[i] += 1

    for j in range(1, len(counter)):
        counter[j] += counter[j-1]

    for k in nums:
        res[counter[k] - 1] = k

    return res


if __name__ == '__main__':
    nums = [6,4,2,1]
    print(countSort(nums))