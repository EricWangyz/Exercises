#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/6/8 22:27   
# @Author  : Eric Wang         
# @File    : 和为S的连续正整数.py        

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res=[]
        for i in range(1,tsum/2+1):
            for j in range(i,tsum/2+2):
                tmp=(j+i)*(j-i+1)/2 # 等差求和公式，首尾相加的和乘以数列长度
                if tmp>tsum:
                    break
                elif tmp==tsum:
                    res.append(range(i,j+1))
        return res