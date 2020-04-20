#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/5/14 20:45   
# @Author  : Eric Wang         
# @File    : 二叉树重建.py        

# 递归的方法
class Solution:

    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        root_node = TreeNode(pre[0])
        i = tin.index(pre[0])
        root_node.left = self.reConstructBinaryTree(pre[1:1+i], tin[:i])
        root_noderight = self.reConstructBinaryTree(pre[1+i:], tin[i+1:])