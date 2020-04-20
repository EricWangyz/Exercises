#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/12 18:54   
# @Author  : Eric Wang         
# @File    : ALi0412.py

f = open("ALi_0412_data.txt", "r")

n = int(f.readline().strip())
k = int(f.readline().strip())
my_list = list(map(int, f.readline().split(",")))
length = len(my_list)

list_sum = 0
for i in range(length):
    list_sum += my_list[i]
print(list_sum)

mean = list_sum // k # 排在前k-l的小二需要管理_mean个酒店
mean_ = mean + 1
left = list_sum % mean  # 排在后面的l的小二需要管理mean_个酒店


def cal_del_len(list_arg):
    list_len = 0
    for x in range(len(list_arg)):
        list_len += len(list_arg[x])
    return list_len


if __name__ == '__main__':
    j = 1
    res = []
    sum_sub = 0
    for m in range(length):
        if j <= k - left:
            sum_sub += my_list[m]
            if sum_sub == mean:
                res.append(my_list[:m + 1])
                j += 1
                sum_sub = 0

        elif j <= k:
            sum_sub += my_list[m]
            if sum_sub == mean_:
                del_len = cal_del_len(res)
                res.append(my_list[del_len: m + 1])
                j += 1
                sum_sub = 0

    print(res)
    for y in range(len(res)):
        print(len(res[y]))
