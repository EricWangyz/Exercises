#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/11/3 22:00   
# @Author  : Eric Wang         
# @File    : 171表列序号.py        

class Solution:
    def titleToNumber(self, s: str) -> int:
        # length = len(s)
        res = 0
        for i,s_ in enumerate(s):
            res = res + 26 ** (len(s) - i - 1) * (ord(s_) - 64)

        return res


if __name__ == '__main__':
    solver = Solution()

    s = "AB"

    print(solver.titleToNumber(s))