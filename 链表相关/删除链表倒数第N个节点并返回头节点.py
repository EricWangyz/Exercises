#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/10 16:10   
# @Author  : Eric Wang         
# @File    : 删除链表倒数第N个节点并返回头节点.py        

class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

    def setnext(self, n_next):
        self.next = n_next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        一次遍历
        :param head:
        :param n:
        :return:
        '''
        dummy = ListNode(0)
        dummy.next = head

        fast, slow = dummy, dummy
        for i in range(n+1):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next

    def removeNthFromEnd2(self,head: ListNode,n: int) -> ListNode:
        '''
        两次遍历，第一次遍历获得链表长度，第二次遍历到相应位置然后进行删除操作
        :param head:
        :param n:
        :return:
        '''
        dummy = ListNode(0)
        dummy.next = head

        length = 0
        index = head
        while index is not None:
            length += 1
            index = index.next

        length = length - n
        index = dummy
        while length > 0:
            length -= 1
            index = index.next
        index.next = index.next.next

        return dummy.next



