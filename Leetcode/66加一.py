#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/11/2 22:04   
# @Author  : Eric Wang         
# @File    : 66加一.py        

class Solution:
    def plusOne(self, digits: list) -> list:
        length = len(digits)
        input_num = 0

        for i in range(length):
            input_num += (10 ** (length - i - 1)) * digits[i]

        output_num = str(input_num + 1)

        return [str(j) for j in output_num]


if __name__ == '__main__':
    input = [1,2,3]

    solver = Solution()

    print(solver.plusOne(input))