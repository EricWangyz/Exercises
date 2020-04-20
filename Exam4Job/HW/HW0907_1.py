#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/7 19:42   
# @Author  : Eric Wang         
# @File    : HW0907_1.py        

nums = [7,5,9,4,2,6,8,3,5,4,3,9]

step = []

for first_step in range(1, len(nums) // 2):
    count = 0
    loc = 0
    loc += first_step
    count += 1

    while loc < len(nums) -1:
        loc += nums[loc]
        count += 1

    if loc == len(nums) -1:
        step.append(count)

    elif loc >= len(nums):
        step.append(-1)

while -1 in step:
    step.remove(-1)

print(min(step))
