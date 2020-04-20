#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/11/3 22:23   
# @Author  : Eric Wang         
# @File    : 172阶乘后面0的个数.py        

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def func(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * func(n - 1)

        mul = str(func(n))[::-1]
        # mul = mul
        # print(mul)
        count = 0
        for i in mul:
            if i == '0':
                count += 1
            else:
                break
        return count


if __name__ == '__main__':
    solver = Solution()
    print(solver.trailingZeroes(7))
