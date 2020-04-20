#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/3/31 22:36   
# @Author  : Eric Wang         
# @File    : 动态规划.py        

'''
 合唱团

有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，
要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？

解题思路：三重循环嵌套 + 动态规划
  第一重循环：对学生数量从1到k进行循环，用i表示学生数量，循环一次得到i个学生以各个编号结尾的最大
或最小乘积（因为可能存在负数），保存在dp中
  第二重循环：对i个学生中的最大编号从i到N进行循环，用j表示最大编号，循环选取新的编号最大的同学
  第三重循环：对以编号j-d到j结尾同学们的最大和者最小乘积进行循环，并将乘积都乘以第j位同学的能力，
  选取新的最大最小乘积，并用该乘积更新dp

'''

N = int(input("please input the length of list(1<= N <=50):"))
input_list = [int(each) for each in input("please input a list(-50 <= a_i <= 50):").split(',')]
k, d = [int(each) for each in input("please input the k(1<= k <=10) and d(1<= d <=50):").split(',')]

dp = [(each, each) for each in input_list]

# 对学生数量从1到k进行循环，用i表示学生数量，循环一次得到i个学生以各个编号结尾的最大
# 或最小乘积（因为可能存在负数），保存在dp中
for i in range(1, k):
    dp_ = dp[:i]

    # 对i个学生中的最大编号从i到N进行循环，用j表示最大编号，循环选取新的编号最大的同学
    for j in range(i, N):
        temp_list = []

        # 对以编号j-d到j结尾同学们的最大和者最小乘积进行循环，并将乘积都乘以第j位同学的能力，
        # 选取新的最大最小乘积，并用该乘积更新dp
        for z in range(j-d, j):
            if z < 0:
                continue
            else:
                temp_list.append(input_list[j]*dp[z][0])
                temp_list.append(input_list[j]*dp[z][1])
        dp_.append((max(temp_list), min(temp_list)))
    dp = dp_

print(max([max(each) for each in dp]))
