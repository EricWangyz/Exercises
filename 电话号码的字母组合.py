#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 20:25
# @Author  : Eric Wang
# @File    : 电话号码的字母组合.py

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution():

    def letterCombinations(self, digits: str) -> [str]:
        phone2letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        output = []

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone2letter[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        if digits:
            backtrack("", digits)
        return output

    def letterCombinations1(self, digits: str) -> [str]:
        m = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz"),
        }
        if not digits:
            return []
        ls1 = [""]
        for i in digits:
            ls1 = [x + y for x in ls1 for y in m[i]]
        return ls1

    def letterCombinations2(self, digits: str) -> [str]:
        phone2letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if not digits:
            return []
        res = [""]
        tmp = [] # 作为临时存储
        for i in digits:
            for s in res:
                for y in phone2letter[i]:
                    tmp.append(s + y)
            res = tmp
            tmp = []  # 清空
        return res


if __name__ == "__main__":
    digits = "23"

    solver = Solution()
    print(solver.letterCombinations1(digits))
