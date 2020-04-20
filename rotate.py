#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/15 21:05   
# @Author  : Eric Wang         
# @File    : rotate.py        


# class Rotate:
#     def rotateMatrix(self, mat, n):
#         # write code here
#         while n<= 300:
#             res = [[] for _ in range(n)]
#             for i in range(n):
#                 for j in range(n):
#
#                     res[i].append(mat[n-j-1][i])
#             return res


# 另一种解法：
# class Rotate:
#     def rotateMatrix(self, mat, n):
#        return [x[::-1] for x in zip(*mat)]
# 利用解包的方法:[[a,b,c],[d,e,f],[g,h,i]]可看成
# [a,d,e],[b,e,h],[c,f,i]三个数组通过zip函数打包而来
# 解包之后反序，即得
def rotateMatrix(matrix):
    # 逆时针旋转矩阵
    global rotate_left
    if matrix:
        reverse = []
        for i in range(len(matrix)):
            reverse.append(list(reversed(matrix[i])))
        rotate_left = [x[::] for x in zip(*reverse)]

    return rotate_left


if __name__ == '__main__':

    # m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    m = [[1]]

    res = []
    for x in m[0]:
        res.append(x)

    while m:
        m = m[1:]
        if not m:
            break
        else:
            m = rotateMatrix(m)
            for k in m[0]:
                res.append(k)
    for res in res:
        print(res)
