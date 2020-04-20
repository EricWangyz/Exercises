#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/7/18 20:15   
# @Author  : Eric Wang         
# @File    : 字符串转换整数.py        

'''
请你来实现一个 atoi 函数，使其能将字符串转换成整数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。
如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

'''

class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        sign_list = ['-','+']
        sign = 0
        res = []
        str = str.strip()
        str = str.rstrip('-+')
        # 输入为空时，返回0
        if str == '':
            return 0
        # 当第一个字符不是数字字符或不是符号时，直接返回0
        if str[0] not in num_list and str[0] not in sign_list:
            return 0

        for i,s in enumerate(str):
            # if s[0] not in num_list and s[0] != '-':
            #     return 0
            if s == '-':
                if i != 0: # 非第一个位置和末尾出现符号
                    return 0
                sign = 1

            elif s == '+':
                if i != 0: # 非第一个位置和末尾出现符号
                    return 0
                sign = 0

            elif s in num_list:
                res.append(s)

            elif s not in num_list:
                break

        resNumStr = ''.join(res)

        if sign:
            # 排除只有一个负号的情况
            if len(resNumStr) == 0:
                return 0
            # 转化为整数
            resNum = - int(resNumStr)
            if resNum >= INT_MIN:
                return resNum
            else:
                return INT_MIN
        else:
            # 排除只有一个正号的情况
            if len(resNumStr) == 0:
                return 0
            resNum = int(resNumStr)
            if resNum <= INT_MAX:
                return resNum
            else:
                return INT_MAX


if __name__ == '__main__':
    str = ['42',
           '-128',
           '-91283472332',
           '0',
           'words and 987',
           '    -42',
           '',
           '-',
           '4193 with',
           '+1',
           '3.14159',
           '+',
           '+-2',           #
           '-+2',           #
           '-5-',           #
           '-13+8'          #
           ]

    solver = Solution()
    for sub_str in str:
        print(solver.myAtoi(sub_str))
