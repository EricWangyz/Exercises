#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/13 20:18   
# @Author  : Eric Wang         
# @File    : 括号生成.py        

class Solution():
    def generateParenthesis(self, n:int)->[str]:
        if n == 0:
            return []
        pre = set({"()",})

        for i in range(n-1):
            now = set()
            for st in pre:
                n = len(st)
                for index in range(n):
                    now.add(st[0:index] + "()" + st[index:n])
            pre = now
        return list(pre)

if __name__ == '__main__':
    solver = Solution()

    print(solver.generateParenthesis(3))