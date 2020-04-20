#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/3/20 16:18   
# @Author  : Eric Wang         
# @File    : 冒泡排序.py

def bubble_sort(unsort_list):
    '''
    从小到大排序
    :param unsort_list:
    :return:
    '''
    for i in range(len(unsort_list) - 1): # 此循环负责冒泡排序的次数
        for j in range(len(unsort_list) - i - 1): #j为列表下标
            if unsort_list[j] > unsort_list[j+1]:
                unsort_list[j], unsort_list[j+1] = unsort_list[j+1], unsort_list[j]
            print(unsort_list)
    return unsort_list

if __name__ == '__main__':
    list = [43,27,8,12,25,3]
    print(bubble_sort(list))


# def bubble_sort1(old_list):
#     for i in range(len(old_list) - 1): # 次数，因为需要与相邻的数做比较，所以是长度减1
#         for j in range(len(old_list) - i - 1): # 下标，一次遍历之后，最大的数冒泡到了最后，
#                                                 # 可以不用管它了，所以数据长度减1
#             if old_list[j] > old_list[j + 1]: # 相邻两个数之间，前者比后者大，则交换
#                 old_list[j], old_list[j+1] = old_list[j+1], old_list[j]
#     return old_list

def bubble(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
    return nums