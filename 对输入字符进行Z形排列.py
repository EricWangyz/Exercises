#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/7/17 20:40   
# @Author  : Eric Wang         
# @File    : 对输入字符进行Z形排列.py        

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        elif numRows == 2:
            s1 = s[0::2]
            s2 = s[1::2]
            return s1 + s2
        elif numRows == 3:
            s1 = s[0::4]
            s2 = s[1::2]
            s3 = s[2::4]
            return s1 + s2 + s3
        elif numRows >= 4:
            tmp = [''] * numRows  # ['','','','',...,'']
            i = 0
            s_len = len(s)
            while i < s_len:
                '''每次循环安置2*numRows个字符'''
                for count_rows in range(numRows):
                    '''将numRows个字符从上往下安置到每一行'''
                    if i < s_len:
                        tmp[count_rows] += s[i]
                        i += 1
                for count_columns in range(numRows - 2, 0, -1):
                    '''将numRows-2个字符从上往下安置到每一行'''
                    if i < s_len:
                        tmp[count_columns] += s[i]
                        i += 1
            res = ''.join(tmp) # 最后进行无缝拼接
            print(tmp)
            return res


if __name__ == '__main__':
    s = "LEETCODEISHIRING"
    numRows = 4

    solver = Solution()
    print(solver.convert(s,numRows))
