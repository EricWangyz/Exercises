#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 21:54
# @Author  : Eric Wang
# @File    : 最长公共前缀.py

"""
题目：
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。


思路：
1、找到字符串列表中长度最小的字符串作为基准
2、列表中的元素逐个与之比较，出现以下情况即返回：
    1出现字符不相匹配的字符串；
    2到达最短字符串的长度，不可能有再长的公共字符串了

"""


class Solution:

    def longestCommonPrefix(self, strList: list) -> str:
        """
        先取最短字符串，然后依次与之比较
        :param strList:
        :return:
        """
        shortestStr = self.shortestStrInList(strList)
        i = 0
        if not strList:
            return ""
        for i in range(len(shortestStr)):
            for j in range(len(strList) - 1):
                if strList[j][i] != strList[j + 1][i]:
                    return strList[j][:i]
        return shortestStr[:i + 1] if len(shortestStr) else ""

    def shortestStrInList(self, strList: list) -> str:
        """
        求一个字符串列表中，长度最短的字符串
        :param strList:
        :return:
        """
        lenList = []
        for s in strList:
            lenList.append(len(s))
        return strList[lenList.index(min(lenList))]


class Solution2:
    """
    另一种思路，利用zip和set特性。
    同时取所有字符串的第一个字符，然后放入一个集合，若长度为1，表明所有的字符相同。
    """
    def longestCommonPrefix(self, strs: list) -> str:
        res = ''
        for s in zip(*strs):
            if len(set(s)) == 1:
                res += s[0]
            else:
                break
        return res



if __name__ == "__main__":
    strList1 = ["flower", "flow", "flight"]
    strList2 = ["dog", "racecar", "car"]

    solver = Solution2()

    print(solver.longestCommonPrefix(strList1))
    print(solver.longestCommonPrefix(strList2))
