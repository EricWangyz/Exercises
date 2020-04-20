#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/5/29 20:41   
# @Author  : Eric Wang         
# @File    : 二叉搜索树的后序遍历是否合法.py

class Solution:
    """
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
    如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
    二叉搜索树的性质：所有的左子树比根节点小，所有的右子树比根节点大。
    后序遍历，最后一个元素即是根。
    去掉最后一个元素，前面一部分都比根节点小，后面一部分都比根节点大。
    同理可求二叉搜索树前序遍历。

    思路:
    1先取最后一个元素，即根节点。
    2然后将剩下的序列分为前后两个部分，如果前面出现比根节点大的，或者后面出现
    比根节点小的元素，直接返回False.
    3将前后部分分别进行递归。结束条件为：左右子树序列长度为0即结束。
    """
    def VerifySquenceOfBST(self, sequence):
        # 序列为空，直接返回false
        if not sequence:
            return False
        # 序列长度为1，说明只有一个根节点，返回true
        if len(sequence)==1:
            return True
        root = sequence[-1]

        i = 0
        while sequence[i] < root:
            i += 1

        for a in range(i, len(sequence)-1):
            if sequence[a] < root:
                return False

        left = sequence[:i]
        right = sequence[i:-2]

        leftIs = True
        rightIs = True

        if len(left) > 0:
            leftIs = self.VerifySquenceOfBST(sequence=left)
        if len(right) > 0:
            rightIs = self.VerifySquenceOfBST(sequence=right)
        return leftIs and rightIs
