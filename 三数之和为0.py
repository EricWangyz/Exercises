#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/8/1 19:29   
# @Author  : Eric Wang         
# @File    : 三数之和为0.py

"""
题目：
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。

思路：
找组合思路：固定三个数字中最左数字的指针 k，遍历 k 找到每个k对应的所有满足nums[k] + nums[i] + nums[j] == 0的 i,j 组合。
即每指向新的 nums[k]，都通过双指针法找到所有和为 00 的 nums[i]，nums[j] 并记录：
当 nums[k] > 0 时直接跳出，因为 j > i > k，即三个数字都大于 00，在此k之后不可能找到组合了；
当 k > 0且nums[k] == nums[k - 1]时跳过此数字k，因为 nums[k - 1] 的所有组合已经被加入到结果中，本次搜索只会搜索到重复组合。
i，j 分设在数组 [k, len(nums)] 两端，根据 sum 与 00 的大小关系交替向中间逼近，如果遇到等于 00 的组合则加入 res 中，需要注意：
移动 i，j 需要跳过所有重复值，以避免重复答案被计入 res。
整体算法复杂度 O(n2)O(n2)。

"""

class Solution:
    def threeSum(self,nums:[int]) -> [[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums)-2):
            if nums[k] > 0: # 如果最小的数大于0，则直接退出，因为nums[k]<nums[i]<nums[j],若最小的数大于0，则三数之和不可能等于0
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i, j = k+1, len(nums)-1 #双指针，将指针设为除k之外的首\尾
            while i < j: # 固定一个数，然后使用双指针，计算三个数的和
                s = nums[k] + nums[i] + nums[j]
                if s < 0: # 如果相加结果小于0，说明数字小了，向右移动左指针，以增大数字，
                    i += 1
                    while i<j and nums[i] == nums[i-1]: # 若移动之后出现相同的数字，则继续移动
                        i += 1
                elif s > 0: # 若结果大于0，则说明数字偏大，则向左移动右指针，减小数字
                    j -= 1
                    while i<j and nums[j] == nums[j+1]: # 若出现相同数字，则继续移动
                        j -= 1
                else:
                    res.append([nums[k],nums[i],nums[j]]) # 当和等于0的时候，将此时的三个数添加到结果列表中
                    i += 1 # 移动指针，
                    j -= 1
                    while i<j and nums[i] == nums[i-1]: # 若移动指针之后，与移动之前的数字相同，则继续移动。
                        i += 1
                    while i <j and nums[j] == nums[j+1]:
                        j -= 1
        return res

if __name__ == '__main__':
    test_list = [-1,0,1,2,-1,-4]

    solver = Solution()
    print(solver.threeSum(test_list))