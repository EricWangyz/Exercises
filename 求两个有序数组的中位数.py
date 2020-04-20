#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/7/14 22:34   
# @Author  : Eric Wang         
# @File    : 求两个有序数组的中位数.py        

class Solution:
    def findMedianSortedArrays(self, num1, num2):
        '''
        先将俩有序数组合并成一个新的有序数组，再求其中位数
        :param num1: list[int]
        :param num2: list[int]
        :return: float
        '''
        res = []

        while len(num1) and len(num2):
            if num1[0] <= num2[0]:
                res.append(num1[0])
                num1.remove(num1[0])
            else:
                res.append(num2[0])
                num2.remove(num2[0])

        if len(num1) == 0:
            res += num2
        elif len(num2) == 0:
            res += num1

        l = len(res)

        if l % 2 == 1:
            return float(res[l // 2])
        elif l % 2 == 0:
            return (res[l // 2 - 1] + res[l // 2 ]) / 2.0

if __name__ == '__main__':
    num1 = []
    num2 = [2,3]

    solver = Solution()
    print(solver.findMedianSortedArrays(num1, num2))

