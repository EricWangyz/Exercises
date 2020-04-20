#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/18 15:57   
# @Author  : Eric Wang         
# @File    : sxf0918.py        

# import sys
# import math
# import numpy as np
# #
# # def print_matrix(matrix):
# #     result = []
# #     while matrix:
# #         result += matrix.pop(0)
# #         if not matrix or not matrix[0]:
# #             break
# #         matrix = turn_matrix(matrix)
# #     return result
# #
# #
# # def turn_matrix(matrix):
# #     num_r = len(matrix)
# #     num_c = len(matrix[0])
# #     newmat1 = []
# #     for i in range(num_c):
# #         newmat2 = []
# #         for j in range(num_r):
# #             newmat2.append(matrix[j][i])
# #         newmat1.append(newmat2)
# #     newmat1.reverse()
# #     return newmat1
#
# class Solution:
#     def printMatrix(self,matrix):
#         res = []
#         while matrix:
#             res += matrix.pop(0)
#             if matrix and matrix[0]:
#                 for row in matrix:
#                     res.append(row.pop())
#             if matrix:
#                 res += matrix.pop()[::-1]
#             if matrix and matrix[0]:
#                 for row in matrix[::-1]:
#                     res.append(row.pop(0))
#         return res
#
#
# if __name__ == '__main__':
#
#     matrix = sys.stdin.readline().strip()
#     str2matrix = []
#     for i in matrix:
#         if i in "0123456789":
#             str2matrix.append(int(i))
#     # print(str2matrix)
#     n = int(math.sqrt(len(str2matrix)))
#
#     # print(n)
#     newmatrix = []
#     for i in range(n):
#         tmp = str2matrix[i*n:(i+1)*n]
#         newmatrix.append(list(tmp))
#     # print(newmatrix)
#     # res_list = print_matrix(newmatrix)
#     res_list = printMatrix(newmatrix)
#
#     for i in range(len(res_list)):
#         if i != len(res_list) -1:
#             print(res_list[i], end=',')
#         else:
#             print(res_list[i],end='')



def solveEqu(eq):
    left,right = eq.split('=')
    lx,lc = solve(left)
    right = solve(right)

def solve(expr):
    x = c = 0
    num, sig = '',1
    for ch in expr+"#":
        if "0" <= ch:
            num += ch
        elif ch == 'k':
            x += int(num or '0') * sig
            num,sig = '',1
            if ch == "-" : sig = -1
    return x,c
