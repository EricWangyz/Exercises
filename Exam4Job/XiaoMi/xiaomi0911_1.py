#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/11 18:53   
# @Author  : Eric Wang         
# @File    : xiaomi0911_1.py        


################## 第二题  ##########################
# while True:
#     N = int(input())
#
#     sumi = 0
#     res = 0
#     for i in range(1,101):
#         sumi = i*(i+1) / 2
#         while sumi == N:
#             res = i
#             break
#     if res == 0:
#         print("No")
#     else:
#         print(res)

###################################################

# while True:
#     N = int(input())
#
#     i = 1
#     while N - i > 0:
#         N -= i
#         i += 1
#         if N < 0:
#             print("No")
#         if N == 0:
#             print(i - 1)

###################################################


# str1 = input()
# str2 = input()
#
#
# if len(str2) == 0:
#     print(str1)
#
# else:
#
#     for s in str2:
#         while s in str1:
#             str1.remove(s)
#
#     print(str1)
#
#
# str1 = str(input())
# str2 = str(input())
#
# if len(str2)==0:
# 	print(str1)
# else:
#
#     for s in str2:
#         while s in str1:
#             str1.replace(s,"")
#
#     print(str1)
#




# str1 = list(map(str, input()))
# str2 = list(map(str, input()))
#
# if len(str1) == 0:
#     print("")
#
# if len(str2) == 0:
#     print(str1)
#
# else:
#
#     for s in str2:
#         for j in str1:
#             if s == j:
#                 str1 = str1.replace(j,"")
#             # str1.remove(s)
#
#     print("".join(str1))







str1 = input()
str2 = input()

if len(str1) == 0:
    print("")

if len(str2) == 0:
    print(str1)
else:
    for s2 in str2:
        for s1 in str1:
            if s2 == s1:
                str1 = str1.replace(s1, "")
            # str1.remove(s)
    print(str1)

