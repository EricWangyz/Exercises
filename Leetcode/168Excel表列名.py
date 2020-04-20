#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/3 16:07
# @Author  : Eric Wang
# @File    : 168Excel表列名.py

n = int(input("请输入一个小于65535的整数："))

res = ""

while n > 0:
    yushu = n % 26
    n = n // 26
    ################
    if yushu == 0:
        n -= 1
        yushu = 26
    #################
    res = chr(64 + yushu) + res


if __name__ == "__main__":
    print(res)
