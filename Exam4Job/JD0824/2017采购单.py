#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/24 15:07   
# @Author  : Eric Wang         
# @File    : 2017采购单.py

while True:
    f = input()
    if f != " ":
        n, m = map(int, f.split())
        prices = [int(x) for x in input().split()]
        # prices = list(map(int, input().split()))

        goods = {}
        for i in range(m):
            good = input()
            if good in goods:
                goods[good] += 1
            else:
                goods[good] = 1

        goods = sorted(goods.items(), key = lambda x: x[1], reverse = True)
        # print(goods)

        prices_min = sorted(prices)
        prices_max = sorted(prices,reverse=True)

        min_sum, max_sum = 0, 0
        for i in range(len(goods)):
            min_sum += goods[i][1] * prices_min[i]
            max_sum += goods[i][1] * prices_max[i]
        print(min_sum,max_sum)
