#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/6/1 22:50   
# @Author  : Eric Wang         
# @File    : 丑数.py        


"""
题目描述：
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

思路：
最直接的暴力解法是从1开始依次判断数字是否为丑数，直到达到要求的丑数个数。
当然这种方法肯定是会TLE的，所以我们分析一下丑数的生成特点(这里把1排除)：

因为丑数只包含质因子2，3，5，假设我们已经有n-1个丑数，按照顺序排列，且第n-1的丑数为M。
那么第n个丑数一定是由这n-1个丑数分别乘以2，3，5，得到的所有大于M的结果中，最小的那个数。

事实上我们不需要每次都计算前面所有丑数乘以2，3，5的结果，然后再比较大小。
因为在已存在的丑数中，一定存在某个数T2T2，在它之前的所有数乘以2都小于已有丑数，而T2×2T2×2的结果一定大于M，
同理，也存在这样的数T3，T5T3，T5，我们只需要标记这三个数即可。

"""
class Solution1:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        # 1作为特殊数直接保存
        baselist = [1]
        min2 = min3 = min5 = 0
        curnum = 1
        while curnum < index:
            minnum = min(baselist[min2] * 2, baselist[min3] * 3, baselist[min5] * 5)
            baselist.append(minnum)
            # 找到第一个乘以2的结果大于当前最大丑数M的数字，也就是T2
            while baselist[min2] * 2 <= minnum:
                min2 += 1
            # 找到第一个乘以3的结果大于当前最大丑数M的数字，也就是T3
            while baselist[min3] * 3 <= minnum:
                min3 += 1
            # 找到第一个乘以5的结果大于当前最大丑数M的数字，也就是T5
            while baselist[min5] * 5 <= minnum:
                min5 += 1
            curnum += 1
        return baselist[-1]


class Solution2:
    def GetUglyNumber_Solution(self, index):
        # write code here

        if index <= 0:
            return 0
        uglyList = [1]
        indexTwo = 0
        indexThree = 0
        indexFive = 0

        for i in range(index - 1):
            newUgly = min(uglyList[indexTwo] * 2, uglyList[indexThree] * 3, uglyList[indexFive] * 5)
            uglyList.append(newUgly)
            if newUgly % 2 == 0:
                indexTwo += 1
            if newUgly % 3 == 0:
                indexThree += 1
            if newUgly % 5 == 0:
                indexFive += 1
        return uglyList[-1]


if __name__ == '__main__':
    solver = Solution1()
    for i in range(10):
        print(solver.GetUglyNumber_Solution(i),end=",")

    # print(solver.GetUglyNumber_Solution(5))