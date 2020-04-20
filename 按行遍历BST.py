#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/5/3 22:16   
# @Author  : Eric Wang         
# @File    : 按行遍历BST.py


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        if not root:
            return []
        stack = [root]
        while stack:
            current = stack.pop(0)

            stack.append(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            return stack