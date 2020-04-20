#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 20:03
# @Author  : Eric Wang
# @File    : 最接近的三数之和.py

"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

"""


class Solution():

    def threeSumClosest(self, nums: [int], target: int) -> int:
        nums.sort() # 先排序
        res = float("inf") # 正无穷
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == target: # 如果刚好等于target，则返回该值
                    return cur_sum

                if abs(res - target) > abs(cur_sum - target): # 如果
                    res = cur_sum
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
        return res


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1

    solver = Solution()
    print(solver.threeSumClosest(nums,target))