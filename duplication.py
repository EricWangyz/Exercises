#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/3/30 22:26   
# @Author  : Eric Wang         
# @File    : duplication.py        

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        nums_len = len(numbers)
        # for i in range(numbers_len - 1):
        #     duplication.append(numbers[i])
        #     for j in range(numbers_len - i - 1):
        #         if numbers[ j+i+1 ] == duplication[0]:
        #             return duplication[0]
        #         else:
        #             duplication.pop(0)
                    # return 0
        for i in range(nums_len-1):
            if numbers[i] in numbers[i+1:]:
                duplication.append(numbers[i])
                break

        return duplication[0]



if __name__ == "__main__":
    solver = Solution()
    list = [2,3,4,6,5,3]
    duplication = []
    # print(duplication)
    num = solver.duplicate(list, duplication)
    print(num)
