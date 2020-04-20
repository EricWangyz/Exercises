#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/7 17:20   
# @Author  : Eric Wang         
# @File    : 删除列表中的奇数项.py        

import random

list_len = 20
list = [random.randint(0, 99) for i in range(list_len)]
print("before:", list)

for i in range(list_len-1, -1, -1):
    if list[i] % 2 == 1:
        del list[i]
    else:
        pass

print("after:", list)
