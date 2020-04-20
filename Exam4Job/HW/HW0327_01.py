#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/3/27 21:24   
# @Author  : Eric Wang         
# @File    : HW0327_01.py        

#0反序输出，1原序输出

import re

str1 = input("第一行数字：")
# str1 = '4'
str2 = input("第二行：")
# str2 = '0qwe1asd0zxc0qaz'

output_str = []

split_str = re.findall('[a-zA-Z2-9]+', str2)
split_num = re.findall('[0-1]+', str2)

if len(split_str) != int(str1) or len(split_num) != int(str1):
    print('输入格式不正确！')

else:
    for i in range(len(split_num)):
        if split_num[i] == '0':
            output_str.append(split_str[i][::-1])

        elif split_num[i] == '1':
            output_str.append(split_str[i])

    for i in range(len(split_str)):
        print(output_str[i], end=' ')
