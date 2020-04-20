#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/3 18:40   
# @Author  : Eric Wang         
# @File    : HW0403_01.py

# 第一题：
# 输入第1行为截取的长度n，第2至N行为要操作的数组。
# 每一次循环依次从第2行至第N行开始每行取n个数，取完即删除。第二次循环接着取数，不够n个数就全部取完。
# 直到所有的都取完，输出最后重新组成的数组。

import sys

if __name__ == "__main__":
    f = open("0403_1.txt",'r')

    # n = int(sys.stdin.readline().strip())
    n = int(f.readline().strip())
    data = []

    while True:
        # line = sys.stdin.readline().strip()
        line = f.readline().strip()
        if not line:
            break
        tmp = list(map(str, line.split(',')))
        data.append(tmp)
    print(data)

    li = [[] for _ in range(len(data))]
    m = len(data)
    max_len = 0
    for i in range(len(data)):
        if len(data[i]) > max_len:
            max_len = len(data[i])
        for j in range(0, len(data[i]), n):
            li[i].append(data[i][j: j + n])
    res = []
    print(li)
    print(max_len)
    for i in range(max_len): # ???
        print(i)
        for j in range(len(data)):
            if len(li[j]) > i:
                res += li[j][i]

    # print(res)
    print(','.join(res))
