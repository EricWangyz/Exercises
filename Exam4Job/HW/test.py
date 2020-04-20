#!/usr/bin/env python
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/7 20:19   
# @Author  : Eric Wang         
# @File    : test.py        

# l1 = [1,1,1,1,1,3,3,3,4]
# print(l1)
#
# print(l1.remove(1))


# str1 = "leeeeeeeetcode"
# #
# # for i in str1:
# #     if i == 'e':
# #         print(str1.replace(i, "-", 1))


while True:
    try:
        n = int(input())
        inputArray = []
        for _ in range(n):
            inputArray.append(int(input()))

        output = sorted((set(inputArray)))
        # sorted(inputSet)

        for j in output:
            print(j)

    except:
        break