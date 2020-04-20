#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/30 11:17   
# @Author  : Eric Wang         
# @File    : 除法.py        

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        global sign
        res = 0

        if abs(dividend) < abs(divisor):
            return 0
        if abs(dividend) == abs(divisor):
            res = 1

        if dividend > 0 and divisor > 0:
            sign = 1
        elif dividend > 0 and divisor < 0:
            sign = 0
        elif dividend < 0 and divisor < 0:
            sign = 1
        elif dividend < 0 and divisor > 0:
            sign = 0

        while abs(dividend) > abs(divisor):
            dividend = abs(dividend) - abs(divisor)
            res += 1

        if sign == 0:
            return 0 - res
        if sign == 1:
            return res


if __name__ == '__main__':
    dividend = -2147483648
    divisor = -1

    solver = Solution()

    res = solver.divide(dividend, divisor)

    print(res)
