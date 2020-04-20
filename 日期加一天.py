#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/29 11:04   
# @Author  : Eric Wang         
# @File    : 日期加一天.py

'''
题目描述
编写一个日期类，要求按xxxx-xx-xx 的格式输出日期，实现加一天的操作。
输入描述:
输入第一行表示测试用例的个数m，接下来m行每行有3个用空格隔开的整数，分别表示年月日。
测试数据不会有闰年。
输出描述:
输出m行。按xxxx-xx-xx的格式输出，表示输入日期的后一天的日期。
'''

m = int(input())


def month(month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        return 28


for i in range(m):
    data = list(map(int, input().split(' ')))
    if data[2]+1 <= month(data[1]):
        print('%d-%02d-%02d' % (data[0], data[1], data[2]+1))
    elif data[2]+1 > month(data[1]) and data[1] < 12:
        print('%d-%02d-01' % (data[0], data[1]+1))
    elif data[2]+1 > month(data[1]) and data[1] == 12:
        print('%d-01-01' % (data[0]+1))
