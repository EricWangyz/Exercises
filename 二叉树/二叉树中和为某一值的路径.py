#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/5/31 15:32   
# @Author  : Eric Wang         
# @File    : 二叉树中和为某一值的路径.py        



class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root: # 如果根节点为空，则返回一个空列表
            return []
        res = []
        if root and not root.left and not root.right and root.val == expectNumber:
            # 如果根节点非空，然后左右子树为空，并且跟根节点处的值刚好等于期望值，则返回路径
            return [[root.val]]
        else:
            left = self.FindPath(root.left, expectNumber-root.val)
            right = self.FindPath(root.right, expectNumber-root.val)

            for i in left+right:
                res.append([root.val]+i)

        return res
