#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 20:02
# @Author  : Eric Wang
# @File    : 合并K个有序链表.py


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    分而治之
    """

    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n - 1)  # 链表列表的首位两个列表进行融合

    def merge(self, lists, left, right):
        """
        # 将长链表分为前后两个短链表，进行递归，最终得到两个链表,然后利用两个链表的融合方式
        :param lists:
        :param left:
        :param right:
        :return:
        """
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        """
        融合两个有序链表
        :param l1:
        :param l2:
        :return:
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
