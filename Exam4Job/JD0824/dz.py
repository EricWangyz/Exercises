#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 20:10
# @Author  : Eric Wang
# @File    : dz.py

n = int(input())
s = input()

dp = [[0, 0] for i in range(n)]

if "A" <= s[0] <= "Z":
    dp[0][0] = 2
    dp[0][1] = 2
else:
    dp[0][0] = 1
    dp[0][1] = 2

for i in range(1, n):
    if "A" <= s[i] <= "Z":
        dp[i][0] = min(dp[i - 1][0] + 2, dp[i - 1][1] + 2)
        dp[i][1] = min(dp[i - 1][0] + 2, dp[i - 1][1] + 1)
    else:
        dp[i][0] = min(dp[i - 1][0] + 1, dp[i - 1][1] + 2)
        dp[i][1] = min(dp[i - 1][0] + 2, dp[i - 1][1] + 2)

print(min(dp[-1][0], dp[-1][1]))
