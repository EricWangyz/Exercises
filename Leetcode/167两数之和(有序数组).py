#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/2 22:42
# @Author  : Eric Wang
# @File    : 167两数之和(有序数组).py


class Solution:

    def twoSum(self, numbers: [int], target: int) -> [int]:
        index1, index2 = 0, len(numbers) - 1

        while index1 < index2:
            num_sum = numbers[index1] + numbers[index2]

            if num_sum == target:
                return [index1 + 1, index2 + 1]
            if num_sum > target:
                index2 -= 1
            elif num_sum < target:
                index1 += 1

        return []


if __name__ == "__main__":
    nums = [2, 7, 8, 9, 11, 12, 22, 33]
    target = 9

    solver = Solution()

    print(solver.twoSum(nums, target))
