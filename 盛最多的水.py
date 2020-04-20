#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/7/29 20:19   
# @Author  : Eric Wang         
# @File    : 盛最多的水.py        

'''
问题：给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

解题：
设置两指针i,j分别位于容器壁两端，逐渐向中间收缩并记录最大值；
每次选定围成水槽两板height[i], height[j]中较小的对应指针，向中间收缩，这是因为：
水槽的高度由两板中的短板决定，每次收缩，都会导致水槽底边宽度-1，
因此，若想找到比当前最大值更大的水槽，那么水槽的短板高必须要高于上一个水槽短板高，而只有向内移动短板，有可能达成这一条件（若移动长板，下个水槽的面积一定小于当前水槽面积）。

'''
class Solution:
    def maxArea(self, height: list) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1

        return res


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]

    solver = Solution()
    print(solver.maxArea(height))