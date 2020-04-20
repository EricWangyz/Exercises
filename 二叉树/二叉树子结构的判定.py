#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/5/28 21:27   
# @Author  : Eric Wang         
# @File    : 二叉树子结构的判定.py        

class Solution:
    # 给定两个二叉树（的根节点）A、B，判断B 是不是A 的二叉树
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False

        result = False
        if pRoot1.val == pRoot2.val:
            result = self.isSubtree(pRoot1, pRoot2)
        if result == False:
            result = self.HasSubtree(pRoot1.left, pRoot2) | self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def isSubtree(self, root1, root2):
        if root2 == None:
            return True
        if root1 == None:
            return False
        if root1.val == root2.val:
            return self.isSubtree(root1.left, root2.left) & self.isSubtree(root1.right, root2.right)
        return False


    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre)==0 | len(tin)==0:
            return None

        root = treeNode(pre[0])
        for order,item in enumerate(tin):
            if root .val == item:
                root.left = self.getBSTwithPreTin(pre[1:order+1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order+1:], tin[order+1:])
                return root

class treeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

if __name__ == '__main__':
    solution = Solution()
    preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    preorder_seq = [1, 2, 3]
    middleorder_seq = [2, 1, 3]
    treeRoot2 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    print(solution.HasSubtree(treeRoot1, treeRoot2))
