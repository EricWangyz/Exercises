#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/9 21:03   
# @Author  : Eric Wang         
# @File    : 求一个数组中的所有组合值等于指定值的组合.py

l = [2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 23, 34, 56]


def combination(l, n):
    l = list(sorted(filter(lambda x: x <= n, l)))
    combination_impl(l, n, [])


def combination_impl(l, n, stack):
    if n == 0:
        print(stack)
        return
    for i in range(0, len(l)):
        if l[i] <= n:
            stack.append(l[i])
            combination_impl(l[i + 1:], n - l[i], stack)
            stack.pop()
        else:
            break

if __name__ == '__main__':
    combination(l, 22)