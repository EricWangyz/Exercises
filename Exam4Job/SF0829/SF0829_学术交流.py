#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 20:57
# @Author  : Eric Wang
# @File    : SF0829_学术交流.py

'''
输入第一行：n,m,k分别表示人数、语言数、知道的信息数
接下来的k行：x_i,y_i表示表示第x_i个人会第y_i种语言。
输入：至少需要多少台翻译机

思路：并查集。
'''
def union_find(nodes:list, edges:list):
    '''
    :param nodes:[0,1,2,3,4,...,n]
    :param edges:[[x_0,y_0],[x_1,x_1],...,[x_k,y_k]]
    :return:
    '''
    father = [0] * len(nodes) # 初始化父节点，初始化的父节点为与下标相同
    for node in nodes:
        father[node] = node

    for edge in edges: # 更新父节点，
        head = edge[0]
        tail = edge[1]
        father[tail] = head

    print("father:", father)

    for node in nodes: # 寻找根节点
        while True:
            father_of_node = father[node]
            if father_of_node != father[father_of_node]:
                father[node] = father[father_of_node]
            else:
                break

    L = {}
    for i, f in enumerate(father):
        L[f] = []
    for i, f in enumerate(father):
        L[f].append(i)

    return L


if __name__ == '__main__':

    # 输入第一行，n,m,k
    input1 = input().split(" ")
    n, m, k = int(input1[0]), int(input1[1]), int(input1[2])

    #输入接下来的k行
    note = []
    for i in range(k):
        a = input().split(" ")
        a = [int(j) for j in a] # 每一行变成列表
        a[0] = a[0] - 1
        note.append(a) # 节点数值减1,note为数值对列表

    print("note:", note)

    output = [] # 下标表示节点，列表元素的值表示父节点，如果子节点相同，则连接在一起。路径压缩
    for i in range(len(note)):
        cur_ = note[i]
        for j in range(i + 1, len(note)):
            if cur_[1] == note[j][1]:
                output.append([cur_[0], note[j][0]])

    print("output:",output)

    nodes = list(range(0, n))

    print("nodes:",nodes)

    L = union_find(nodes, output)

    print(len(L) - 1)


'''
8 4 10
1 1
2 1
3 1
4 1
3 2
5 2
6 3
7 3
5 4
8 4
'''

'''
3 3 2 
2 3
3 1
'''