#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/6/9 16:49   
# @Author  : Eric Wang         
# @File    : 扑克牌顺子.py        

# LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
# 他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
# “红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....
# LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
# 上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
# LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
# 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        l = len(numbers)
        if l < 5:
            return False

        numOfZero = 0
        nums = sorted(numbers)
        for i in range(4):
            if nums[i] == 0:
                numOfZero += 1  # 计算0的个数，
        if numOfZero == 4:  # 若出现4个0,则肯定能凑成顺子。
            return True

        total_gap = 0  # 计算总的间隔
        for j in range(numOfZero, 4):
            if nums[j] == nums[j + 1]:
                return False  # 若出现相等的情况，直接返回false
            total_gap += (nums[j + 1] - nums[j] - 1)

        if total_gap <= numOfZero:  # 总的间隔数少于或等于0的个数，返回ture，0可以充当任意数字
            return True
        else:
            return False