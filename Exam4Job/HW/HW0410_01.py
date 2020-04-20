#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/10 20:12   
# @Author  : Eric Wang         
# @File    : HW0410_01.py        

str_input = list(input().split(" "))

N = 8
print(str_input)
n = int(str_input[0])
str = str_input[1:]
print(str)


result = [[] for _ in range(n)]

for i in range(n):# 字符串计数,第i个字符串
    k = len(str[i]) // 8 # 字符串长度除
    l = len(str[i]) % 8
    print(k, l)
    # str[i]
    data = [[] for _ in range(k+1)]
    for j in range(k):
        data[j].append(str[i][8*j : 8*(j+1)])
        result[i].append(data)

    if l > 0:
        data[-1].append(str[i][8*k:] + "0" * (N -l))
        result[i].append(data)
    else:
        pass

for m in range(len(result)):
    print(result[m])



if __name__ == '__main__':
     pass