#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/6/8 21:36   
# @Author  : Eric Wang         
# @File    : 平衡二叉树.py        

"""
平衡二叉搜索树（Self-balancing binary search tree）又被称为AVL树（有别于AVL算法），
且具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，
并且左右两个子树都是一棵平衡二叉树。
"""


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)


    def TreeDepth(self, pRoot):
        # 计算树的深度
        if not pRoot:
            return 0
        else:
            right_depth = self.TreeDepth(pRoot.right)
            left_depth = self.TreeDepth(pRoot.left)
        return max(right_depth, left_depth) + 1