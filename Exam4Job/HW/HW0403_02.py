#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/3 20:53   
# @Author  : Eric Wang         
# @File    : HW0403_02.py

# 第二题：
# 输入一些串字符，，合法字符为0-9a-zA-Z，其余的为非法字符
# 输出一反序的合法字符
# 输出二非法字符
# 输出三左移之后的合法字符
# 输出四左移完成之后排序的合法字符

import re

all_strings = list()
valid_strings = list()
invalid_strings = list()
while True:
    try:
        s = input("input:").strip()
        if re.match('[0-9a-zA-Z]+$',s):
            if s not in valid_strings:
                valid_strings.append(s)
        else:
            invalid_strings.append(s)
    except EOFError:
        break

new_valid_strings = list()

for s in valid_strings:
    shift = 10 % len(s)
    new_s = s[shift:] + s[:shift]
    new_valid_strings.append(new_s)

print(' '.join(valid_strings))
print(' '.join(invalid_strings))
print(' '.join(new_valid_strings))
print(' '.join(sorted(new_valid_strings)))