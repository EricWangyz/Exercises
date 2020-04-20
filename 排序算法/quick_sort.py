#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/3/21 19:57   
# @Author  : Eric Wang         
# @File    : quick_sort.py        

import random

RANGE = 100
LENGTH = 5
my_list = random.sample(range(RANGE), LENGTH)

print('before sort:', my_list)


def quickSort(myList, start, end):
    if start < end:
        i, j = start, end
        # 设置基准数
        base = myList[i]

        while i < j:
            # 如果列表最后的数比基准数大或相等，则前移一位直到出现比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j -= 1
            # 找到比基准数小的数，则将这个第j个数复制给第i个数，此时表中第i，j个元素的值相等
            myList[i] = myList[j]
            # print('1:', myList)

            # 同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i += 1
            myList[j] = myList[i]
            # print('2:', myList)

        # 做完一轮比较之后，列表被分为两个半区，并且i=j，需要将这个数设置为base
        myList[i] = base
        # print('3:', myList)

        # 递归前后半区
        quickSort(myList, start, i - 1)
        quickSort(myList, j + 1, end)

    return myList


def quick_sort(sorting, left, right):
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        # 将小于中轴值的元素放在列表前面
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            # a右移一位
            a += 1
            i += 1
        # 将大于中轴值的元素放在列表后面
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            # b左移一位
            b -= 1
        else:
            # 继续比较下一个元素
            i += 1
        # print(sorting)  看输出结果便能很好理解
    # 循环结束后a=b=i
    # 递归对左半部分进行快速排序
    quick_sort(sorting, left, a - 1)
    # 递归对右半部分进行快速排序
    quick_sort(sorting, b + 1, right)



if __name__ == '__main__':
    # my_list = [2,1]
    print(quickSort(my_list, 0, len(my_list) - 1))
    # quick_sort(my_list, 0, len(my_list) - 1)
    # print('after sort:', my_list)
