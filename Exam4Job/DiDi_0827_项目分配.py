#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/27 20:11   
# @Author  : Eric Wang         
# @File    : DiDi_0827_项目分配.py

INPUT = list(map(int, input().split()))

N = INPUT[0]
M = INPUT[1]

matrix = []
max_Aij = []

for i in range(N):
    A_j = list(map(int, input().split()))
    matrix.append(A_j)
# print(matrix)

matrix_rotate = zip(*matrix)

for j in matrix_rotate:
    max_Aij.append(max(j))
    max_Aij.sort(reverse=True)
# print(max_Aij)

if M > N:
    result = sum(max_Aij)
else:
    result = sum(max_Aij[0:M])
print(result)
