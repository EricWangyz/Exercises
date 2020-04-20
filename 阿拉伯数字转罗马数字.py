#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 20:34
# @Author  : Eric Wang
# @File    : 阿拉伯数字转罗马数字.py

"""
题目：
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

"""


class Solution:

    def intToRoman(self, num: int) -> str:
        """
        阿拉伯数字转罗马数字

        思路：
        将整数转化为roman字符串，总体思路是先处理高位字符，舍去高位后再处理低位字符。
        如1437，先将1000的字符加入，再处理437，将400字符加入，再处理37……
        有两种特例需要处理9xx，4xx，但总体上还是可以约化为先处理高位再处理低位的问题，如1900，先加入1000，再加入特例900……
        开辟两个数组分别存储数字和对应字符，对num处理算出当前位需要几个字符，k++遍历下个字符，直到num = 0时返回。
        """
        res = ""
        ROMAN = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        INT = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        while num > 0:
            count = num // INT[i]
            res += "".join([ROMAN[i] for _ in range(count)])
            num -= count * INT[i]
            i += 1
        return res

    def romanToInt(self, romanNum: str) -> int:
        """
        罗马数字转阿拉伯数字

        思路：
        从左往右一位一位的看，如果这一位数字比它右边一位的数字大或与其相等，则加上这一位代表的值，
        如果它比右边一位小，则减去这一位代表的数字。
        """
        ROMAN_NUMS = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        intNum = 0
        for i in range(len(romanNum) - 1):
            if ROMAN_NUMS[romanNum[i]] >= ROMAN_NUMS[romanNum[i + 1]]:
                intNum += ROMAN_NUMS[romanNum[i]]
            else:
                intNum -= ROMAN_NUMS[romanNum[i]]

        intNum += ROMAN_NUMS[romanNum[-1]]
        return intNum


if __name__ == "__main__":
    nums = [123, 456, 7, 23456, 951]
    roman_nums = ["CXXIII", "CDLVI", "VII", "MMMMMMMMMMMMMMMMMMMMMMMCDLVI", "CMLI"]

    solver = Solution()
    print("==========intToRoman===========")
    for j in nums:
        print(solver.intToRoman(j))

    print("==========romanToInt===========")
    for k in roman_nums:
        print(solver.romanToInt(k))
