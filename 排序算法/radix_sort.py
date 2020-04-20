#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/3/21 22:49   
# @Author  : Eric Wang         
# @File    : radix_sort.py        


def radix_sort(list, d=3): #默认为3位数的排序，d表示排序数的位数
    # global result
    for i in range(d):
        # 每一位数字都是0-9，建10个桶
        s = [[] for k in range(10)]
        for j in list:
            # 遍历所要排序列表中的数字，进入循环，分别获取个位、十位、百位上的数字，并分别添加到相应的桶中
            s[(j // (10 ** i)) % 10].append(j)

        print('第'+ str(i) +'次遍历结果:', s)
        # 提取各个桶中的数据，构成新的列表，用于下次循环的时候遍历。
        list = [a for b in s for a in b]

    return list

if __name__ == '__main__':
    my_list = [852, 456, 258, 789, 741, 963]
    output_list = radix_sort(my_list)
    print('after sort:', output_list)
