#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/11/2 22:55   
# @Author  : Eric Wang         
# @File    : 155最小栈.py        

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.helperStack = [] #辅助栈

    def push(self, x: int) -> None:
        self.minStack.append(x)
        if not self.helperStack or x <= self.helperStack[-1]:
            self.helperStack.append(x)

    def pop(self) -> None:
        if self.minStack.pop() == self.helperStack[-1]:
            self.helperStack.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.helperStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()