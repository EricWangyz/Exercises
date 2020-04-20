#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/22 22:55   
# @Author  : Eric Wang         
# @File    : 日期推算.py

def runnian(year):
    if (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def month_total(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if runnian(year):
            return 29
        else:
            return 28

if __name__ == '__main__':
    m = int(input())
    for i in range(m):
        time = input().split()
        year = int(time[0])
        month = int(time[1])
        day = int(time[2]) + int(time[3])

        while day > month_total(year, month):
            day -= month_total(year, month)
            month += 1
            if month > 12:
                year += 1
                month -= 12

        print("%d-%02d-%02d" % (year, month, day))
