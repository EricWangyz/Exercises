#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/13 21:52   
# @Author  : Eric Wang         
# @File    : 链表反转.py        

class ListNode():
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution():
    def reverseLinkList(self, head):
        if head == None or head.next == None:
            return head
        Node = None
        while head:
            p = head
            head = head.next
            p.next = Node
            Node = p
        return Node
