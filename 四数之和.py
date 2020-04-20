#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/10 15:55   
# @Author  : Eric Wang         
# @File    : 四数之和.py        

class Solution(object):
    def fourSum(self, nums: [int], target: int) -> list:
        '''
        固定前两个数，然后利用双指针法
        :param nums:
        :param target:
        :return:
        '''
        nums.sort()
        res = set()

        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j+1
                right = len(nums)-1
                while(left < right):
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp == target:
                        res.add((nums[i],nums[j],nums[left],nums[right]))
                        left += 1
                        right -= 1
                    if temp > target:
                        right -= 1
                    if temp < target:
                        left += 1
        result = []
        for k in res:
            result.append(list(k))
        return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    solver = Solution()
    print(solver.fourSum(nums,target))
