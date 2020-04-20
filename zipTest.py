#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 22:07
# @Author  : Eric Wang
# @File    : zipTest.py


# class Printer:
#     def clockwisePrint(self, mat,n,m):
#         # write code here
#         res = []
#         while len(mat) > 0:
#             for i in range(len(mat[0])):
#                 res.append(mat[0][i])
#             mat =[x for x in zip(*mat[1:])][::-1]
#         return res
#
#
# if __name__ == '__main__':
#     a = [[1,2,3], [4,5,6], [7,8,9]]
#     b = Printer()
#     print(b.clockwisePrint(a,0,0))


class FoldPaper:

    def foldPaper(self, n):
        res = []

        def midTraversal(n, postion):  # 使用中序遍历
            if n == 0:
                return
            midTraversal(n - 1, "left")
            if postion == "left":
                res.append("down")
            else:
                res.append("up")
            midTraversal(n - 1, "right")

        midTraversal(n, "left")
        return res


if __name__ == "__main__":
    a = FoldPaper()
    print(a.foldPaper(3))
