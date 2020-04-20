#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/6/1 21:18   
# @Author  : Eric Wang         
# @File    : 最大连续子序列和——动态规划.py        

"""
给定数字序列，求连续子向量的最大和。
例如，给定[-2, 6, -1, 5, 4, -7, 2, 3]，其最大的连续子序列的和为第2个数字到第5个数字的和14

解题思路：
动态规划。复杂度为 O(n)
步骤 1：令状态 dp[i] 表示以 A[i] 作为末尾的连续序列的最大和（这里是说 A[i] 必须作为连续序列的末尾）。
步骤 2：做如下考虑：因为 dp[i] 要求是必须以 A[i] 结尾的连续序列，那么只有两种情况：

这个最大和的连续序列只有一个元素，即以 A[i] 开始，以 A[i] 结尾。
这个最大和的连续序列有多个元素，即从前面某处 A[p] 开始 (p<i)，一直到 A[i] 结尾。
　　对第一种情况，最大和就是 A[i] 本身。
　　对第二种情况，最大和是 dp[i-1]+A[i]。
　　于是得到状态转移方程：
　　　　　　　　dp[i] = max{A[i], dp[i-1]+A[i]}
　　这个式子只和 i 与 i 之前的元素有关，且边界为 dp[0] = A[0]，
由此从小到大枚举 i，即可得到整个 dp 数组。接着输出 dp[0]，dp[1]，...，dp[n-1] 中的最大子即为最大连续子序列的和。
"""

if __name__ == '__main__':
    array = list(input("输入数组（请以逗号隔开）："))
    print(array)

    array_list = []
    for s in array:
        array_list.append(int(s))

    dp = [] # 建立一个存放每一步最大的列表
    dp.append(array_list[0])
    for i in range(1, len(array_list)):
        dp.append(max(array_list[i], array_list[i] + dp[i-1]))
    print(max(dp))
