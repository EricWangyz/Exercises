#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/7/17 21:42   
# @Author  : Eric Wang         
# @File    : 反转有符号的整数.py        

class Solution1:
    def reverse(self, x: int) -> int:
        Min = - 2**31
        Max = 2**31 -1

        x = str(x)

        if x[0] == '-':
            x = x[1:]
            x = x[::-1]

            for i,s in enumerate(x):
                if s != '0':
                    x = x[i:]
                x = -int(x)
                if Min <= x and x <= Max:
                    return x
                else:
                    return 0
        else:
            x = x[::-1]
            for i,s in enumerate(x):
                if s != '0':
                    x = x[i:]
                re = int(x)
                if Min <= re and re <= Max:
                    return re
                else:
                    return 0


class Solution2:
    def reverse(self, x: int) -> int:
        Min = - 2 ** 31
        Max = 2 ** 31 - 1

        if x == 0:
            return 0

        y = str(abs(x))
        # print(type(y))
        y = int(y[::-1].lstrip('0'))
        # print(y)
        # for i,s in enumerate(y):
        #     if s != '0':
        #         y = y[i:]
        if x < 0:
            if -y >= Min and -y <= Max:
                return -y
            else:
                return 0
        if x > 0:
            if y >= Min and y <= Max:
                return y
            else:
                return 0

if __name__ == '__main__':
    nums = [-230, -2147483648, 0]
    solver = Solution2()
    for num in nums:

        print(solver.reverse(num))
