#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/5/31 19:30   
# @Author  : Eric Wang         
# @File    : test.py        

# #%%
# import numpy as np
#
# # 公式：newValue = (oldValue-min)/(max)
# group = np.array([[1, 7, 3],
#                   [1, 3, 1],
#                   [0, 5, 8],
#                   [2, 7, 3]])
# minVals = group.min(0)  # 为0时：求每列的最小值[0 3 1]   .shape=(3,)
# maxVals = group.max(0)  # 为0时：求每列的最大值[2 7 8]   .shape=(3,)
# ranges = maxVals - minVals
#
# m = group.shape[0]
# normDataSet = np.zeros(np.shape(group))  # np.shape(group) 返回一个和group一样大小的数组，但元素都为0
# diffnormData = group - np.tile(minVals, (m, 1))  # (oldValue-min)  减去最小值
# normDataSet1 = diffnormData / np.tile(ranges, (m, 1))
#
# print(minVals)  # 打印最小值 [0 3 1]
# print(maxVals)  # 打印最大值 [2 7 8]
# print(normDataSet1)

#%%
class Solution1():
    def __init__(self):
        pass

    def who_am_i(self):
        print("阿黄")

class Solution2():

    def who_am_i(self):
        print("阿磊")

if __name__ == '__main__':
    solver1 = Solution1()
    solver1.who_am_i()

    solver2 = Solution2()
    solver2.who_am_i()
