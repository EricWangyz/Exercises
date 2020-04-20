#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/6/10 15:30   
# @Author  : Eric Wang         
# @File    : 不使用循环从1加到n.py        

class solution:
    def add_no_circum(self, n):
        return n > 0 and n + self.add_no_circum(n-1)


if __name__ == '__main__':
    solver = solution()
    print(solver.add_no_circum(5))