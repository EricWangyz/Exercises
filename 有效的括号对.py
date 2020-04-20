#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/10 22:37   
# @Author  : Eric Wang         
# @File    : 有效的括号对.py        

class Solution(object):
    def isValid(self, s):
        '''
        利用堆栈，
        :param s:
        :return:
        '''
        stack = []
        judge = {'()','[]','{}'}

        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] + i in judge:
                    stack.pop()
                else:
                    stack.append(i)

        return stack == []

if __name__ == '__main__':
    s = "()[]{}"

    solver = Solution()
    print(solver.isValid(s))