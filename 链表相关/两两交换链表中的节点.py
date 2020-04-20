#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/13 21:08   
# @Author  : Eric Wang         
# @File    : 两两交换链表中的节点.py        

class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution():
    def swapPairs(self, head: ListNode):
        dummy = ListNode(0)
        p = dummy
        h = head
        while h:
            if h and h.next:
                tmp = h.next
                p.next = tmp

                h.next = h.next.next
                tmp.next = h
                h = h.next
                p = p.next.next

            else:
                p.next = h
                h = h.next

        return dummy.next