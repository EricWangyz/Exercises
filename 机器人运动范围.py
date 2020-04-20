#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/6/16 22:50   
# @Author  : Eric Wang         
# @File    : 机器人运动范围.py        

"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下
四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""

class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        # write code here
        arr = [[1 for i in range(cols)] for j in range(rows)]
        self.findway(arr, 0, 0, threshold)
        return self.count

    def findway(self, arr, i, j, k):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            return
        tmpi = list(map(int, list(str(i))))
        tmpj = list(map(int, list(str(j))))
        if sum(tmpi) + sum(tmpj) > k or arr[i][j] != 1:
            return
        arr[i][j] = 0
        self.count += 1
        self.findway(arr, i + 1, j, k)
        self.findway(arr, i - 1, j, k)
        self.findway(arr, i, j + 1, k)
        self.findway(arr, i, j - 1, k)


from collections import deque


class Solution2:
    def get_sum(self, x):
        res = 0
        while x:
            res += x % 10
            x = x // 10
        return res

    def is_valid(self, x, y, m, n, k):
        """
        :param x: 表示当前行index
        :param y: 表示当前列index
        :param m:表示行范围
        :param n:列范围
        :param k:行列之和最大值限制
        :return:
        """
        return 0 <= x < m and 0 <= y < n and self.get_sum(x) + self.get_sum(y) <= k

    def movingCount(self, threshold, rows, cols):
        self.memo = {}
        self.m = rows
        self.n = cols
        self.k = threshold
        return self.dfs(0, 0)

    def dfs(self, x, y):
        '''
        是否进行回溯，取决于状态是什么，23题因为需要还原状态
        取决于状态是什么，我们需要保证对于DFS的每个分支，递归下去的时候看到的状态都是相同的。
        '''
        # 如果不在合法范围区域 ，返回0
        if not self.is_valid(x, y, self.m, self.n, self.k):
            return 0
        # 如果访问过，返回0，防止重复添加
        if (x, y) in self.memo:
            return 0
        # 否则，标记为访问过
        self.memo[(x, y)] = 1
        # 递归调用，上右下左的结果，最后加上当前本身的位置，也就是+1
        return self.dfs(x - 1, y) + self.dfs(x, y - 1) + self.dfs(x + 1, y) + self.dfs(x, y + 1) + 1
