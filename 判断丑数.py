#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 21:05
# @Author  : Eric Wang
# @File    : 判断丑数.py


class Solution():

    def isUgly(self, num):
        if num <= 0:
            return False
        elif num == 1:
            return True

        while num > 1:
            # if...:elif...: elif...: 用于互斥条件的条件分支，每次只执行一个条件的语句
            if num % 2 == 0:
                num /= 2

            elif num % 3 == 0:
                num /= 3

            elif num % 5 == 0:
                num /= 5

            else:
                return False
        return True


if __name__ == '__main__':
    solver = Solution()
    # print(solver.isUgly(7))

    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    vali = [1,1,1,1,1,1,0,1,1,1,0,1,0]
    res = []

    for i in nums:
        res.append(solver.isUgly(i))
    print(res)
    print(res==vali)
