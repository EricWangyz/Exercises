#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/6/1 21:42   
# @Author  : Eric Wang         
# @File    : 1-n之间1出现的次数.py        

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1, n+1):
            count += str(i).count("1")
        return count


if __name__ == '__main__':
    # 字符查找计数函数str.count()
    solver = Solution()
    a = input("please input N:")
    res = solver.NumberOf1Between1AndN_Solution(a)
    print(res)