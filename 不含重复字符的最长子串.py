#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/7/14 22:03   
# @Author  : Eric Wang         
# @File    : 不含重复字符的最长子串.py
from typing import Dict, Any


class Solution:
    '''
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''

        :param s: type str
        :return: type int
        '''
        usedchar = {}
        start = res = 0
        for index, char in enumerate(s):
            if char in usedchar and start <= usedchar[char]:
                start = usedchar[char] + 1
            else:
                res = max(res, index - start + 1)
            usedchar[char] = index

        return res


class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not len(s): return 0
        dp=[1]*len(s) # 构建一个长度和字符串长度相同的列表，列表元素全部为1
        tmp=s[0] # 取字符串的第一个为起点作为比较对象
        for i in range(1,len(s)):
            if s[i] in tmp:
                # 如果下一个字符s在tmp中，则找到s在tmp中的下标，将其下一个作为下一次寻找的起点
                idx=tmp.index(s[i])
                tmp=tmp[idx+1:]+s[i] #将其也包含进来
            else:
                tmp+=s[i]
            dp[i]=max(len(tmp),dp[i]) #每次迭代都记录当前的最大长度
        return max(dp) # 最后返回每一步长度最大的


if __name__ == '__main__':

    s = 'pwwkew'

    solver = Solution1()
    print(solver.lengthOfLongestSubstring(s))
