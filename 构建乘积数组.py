#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/6/10 22:48   
# @Author  : Eric Wang         
# @File    : 构建乘积数组.py        

"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。

"""

class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
            res = 1
            for j, value in enumerate(A):
                if j == i:
                    continue
                res = res * value
            B.append(res)
        return B