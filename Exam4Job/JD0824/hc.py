#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 20:45
# @Author  : Eric Wang
# @File    : hc.py

N = int(input())
H = list(map(int, input().split()))

last = [1000000000000] * N
last[-1] = H[-1]
first = [0] * N
first[0] = H[0]

for i in range(N - 2, -1, -1):
    if H[i] < last[i+1]:
        last[i] = H[i]
    else:
        last[i] = last[i + 1]

for i in range(1, N):
    if H[i] > first[i - 1]:
        first[i] = H[i]
    else:
        first[i] = first[i - 1]

last.append(0)
first.insert(0, 0)

res = 0
for i in range(N + 1):
    if first[i] <= last[i]:
        res += 1
print(res)
