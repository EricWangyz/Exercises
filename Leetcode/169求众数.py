#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/11/3 21:30   
# @Author  : Eric Wang         
# @File    : 169求众数.py        

class Solution():
    def majorityNum1(self, nums:[int]) -> int:
        '''
        暴力法
        :param nums:
        :return:
        '''
        nums_set = set(nums)
        for i in nums_set:
            if nums.count(i) > len(nums) // 2:
                return i

    def majorityNum2(self, nums:[int]) -> int:
        '''
        再来回顾一下题目：寻找数组中超过一半的数字，这意味着数组中其他数字出现次数的总和都是比不上这个数字出现的次数 。

        即如果把 该众数记为 +1 ，把其他数记为 −1 ，将它们全部加起来，和是大于 0 的。

        所以可以这样操作：

        设置两个变量 candidate 和 count，candidate 用来保存数组中遍历到的某个数字，count 表示当前数字的出现次数，
        一开始 candidate 保存为数组中的第一个数字，count 为 1
        遍历整个数组
        如果数字与之前 candidate 保存的数字相同，则 count 加 1
        如果数字与之前 candidate 保存的数字不同，则 count 减 1
        如果出现次数 count 变为 0 ，candidate 进行变化，保存为当前遍历的那个数字，并且同时把 count 重置为 1
        遍历完数组中的所有数字即可得到结果
        :param nums:
        :return:
        '''
        candidate, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]

            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == '__main__':
    nums = [1,1,1,2,2,2,2,3,3,3,3,3,3,3,3]
    nums2 = [2,2,1,1,1,2,2]
    nums3 = [3,2,3]
    solver = Solution()

    print(solver.majorityNum1(nums3))
    print(solver.majorityNum2(nums3))

    # print(nums.count(3))