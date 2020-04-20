#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/3/25 22:35   
# @Author  : Eric Wang         
# @File    : bucket_sort.py        


def bucket_sort(list, n):
    # 创建n个桶
    bucket = [[] for _ in range(n)]

    # 将list插入bucket
    for data in list:
        index = int(data * n)
        bucket[index].append(data)

    # 桶内排序
    for i in range(n):
        bucket[i].sort()

    # 产生新的排序后的列表
    index = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            list[index] = bucket[i][j]
            index += 1
    return list


def main():
    test_list = [0.897, 0.565, 0.656, 0.123, 0.665, 0.3434]
    n = len(test_list)
    result = bucket_sort(list, n)
    print(result)


if __name__ == "__main__":
    main()
