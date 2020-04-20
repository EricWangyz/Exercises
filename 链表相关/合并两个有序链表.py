#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/12 19:50   
# @Author  : Eric Wang         
# @File    : 合并两个有序链表.py        

class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        递归
        :param l1:
        :param l2:
        :return:
        '''
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2