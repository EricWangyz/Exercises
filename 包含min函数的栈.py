#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/5/28 21:33   
# @Author  : Eric Wang         
# @File    : 包含min函数的栈.py        

'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
（时间复杂度应为O（1））。
'''


class Solution:
    def __init__(self):
        # 初始化一个栈
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        # 压入操作。
        self.stack.append(node)
        # min_stack为空，则先压入一个元素，当后续出现比第一个元素小的元素时，继续压入
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        # 如果要弹出的是当前最小的，则min_stack中也要跟着弹出
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self): #
        # 获取栈顶元素
        return self.stack[-1]

    def min(self):
        # 返回当前栈中最小元素
        return self.min_stack[-1]
