#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/9 20:19   
# @Author  : Eric Wang         
# @File    : xingyunzhe.py        

m = int(input('总数：'))
p = []
out = 0
index = 0
res_list = []
if(m>0 and m<=10000):
    for i in range(1,m+1):
        p.append(i)
    while(len(p) > 1):
        out += 1
        index += 1
        if (index > len(p)):
            index = 1
        if(out == 5):
            out = 0

            # res_list.append(index-1)

            p.pop(index-1)

            index -= 1
    print(res_list)
    print("Last No. is", p[0])
else:
    print(m, "is out of range of valid values.")
