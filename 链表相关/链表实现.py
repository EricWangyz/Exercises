#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/7 19:49   
# @Author  : Eric Wang         
# @File    : 链表实现.py        

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def setnext(self, n_next):
        self.next = n_next

class Linklist():
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.ListNode = []
        self.ListValue = []

    def addnode(self, value):
        #添加
        node = Node(value)
        self.tail.setnext(node)
        self.tail = node

    def getnode(self, node):
        return node.value, node.next

    def traversing(self):
        # 遍历
        self.ListNode=[]
        self.ListValue=[]
        value, n_ext = self.getnode(self.head)
        self.ListNode.append(self.head)
        self.ListValue.append(value)
        while (n_ext):
            self.ListNode.append(n_ext)
            value, n_ext = self.getnode(n_ext)
            self.ListValue.append(value)

    def insertnode(self,node1, node2, value):
        #插入
        node = Node(value)
        node1.setnext(node)
        node.setnext(node2)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    head = Node(1)
    linkList = Linklist(head)
    for i in range(len(data) - 1):
        linkList.addnode(data[i + 1])
    linkList.traversing()
    print(len(linkList.ListValue))
    print(len(linkList.ListNode))
    print(linkList.ListValue)
    print(linkList.ListNode)

    linkList.insertnode(linkList.ListNode[4],linkList.ListNode[5],6)
    linkList.traversing()
    print(len(linkList.ListValue))
    print(len(linkList.ListNode))
    print(linkList.ListValue)
    print(linkList.ListNode)
