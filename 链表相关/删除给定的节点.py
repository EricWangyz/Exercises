#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/10 22:28   
# @Author  : Eric Wang         
# @File    : 删除给定的节点.py        

class Solution:
    def deleteNode(self, node):
        '''
        由于只输入了需要删除的节点node，因此无法获取删除节点node的前一个节点pre，从而也就无法将前一个节点pre指向删除节点的下一个节点nex；
        既然无法通过修改指针完成，那么肯定要修改链表节点的值了。
        将删除节点node的值和指针都改为下一个节点nex的值和指针即可。
        :param node:
        :return:
        '''
        node.val = node.next.val
        node.next = node.next.next

