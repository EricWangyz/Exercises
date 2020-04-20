#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 19:09
# @Author  : Eric Wang
# @File    : HW0904_01.py


n = int(input())

res_list = []

for i in range(50):
    for j in range(23):
        if (i * 4 + j * 9) == n:
            res_list.append(i + j)

if res_list is not None:
    print(min(res_list))
else:
    print(-1)




    def divide(self, divd: int, dior: int) -> int:
        res = 0
        sign = 1 if divd ^ dior > 0 else -1
        divd = abs(divd)
        dior = abs(dior)
        while divd >= dior:
            res += 1
            divd -= dior
        res = res * sign
        return min(max(-2 ** 31, res), 2 ** 31 - 1)

class Solution:
    def divide(self, divd: int, dior: int) -> int:
        res = 0
        sign =  1 if divd ^ dior >= 0 else -1
        #print(sign)
        divd = abs(divd)
        dior = abs(dior)
        while divd >= dior:
            tmp, i = dior, 1
            while divd >= tmp:
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign
        return min(max(-2**31, res), 2**31-1)

