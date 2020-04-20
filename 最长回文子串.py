#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/7/15 19:41   
# @Author  : Eric Wang         
# @File    : 最长回文子串.py        

class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_length = len(s)
        max_length = 0
        start = 0
        for i in range(str_length):
            if i - max_length >= 1 and s[i - max_length - 1:i+2] == s[i-max_length-1:i+2][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i-max_length:i+2] == s[i-max_length:i+2][::-1]:
                start = i - max_length
                max_length += 1
            return s[start:start + max_length+1]


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        res = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                l, r = i - 1, i
                while l >= 0 and r <= len(s) - 1:
                    if s[l] != s[r]:
                        break
                    l -= 1
                    r += 1
                res = s[l + 1:r] if len(s[l + 1:r]) > len(res) else res
            l, r = i - 1, i + 1
            while l >= 0 and r <= len(s) - 1:
                if s[1] != s[r]:
                    break
                l -= 1
                r += 1
            res = s[l + 1:r] if len(s[l + 1:r]) > len(s) else res

        return res


# import numpy as np

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        s_len =len(s)
        if s_len == 1:
            return s
        if s_len == 2 and s[0] == s[1]:
            return s

        isLongestPalindrome = [[[0] * s_len] * s_len]
        maxLen = 0
        startIndex = 0
        endIndex = 0

        for i in range(s_len):
            j = i
            while j >= 0:
                if s[i] == s[j] and (i-j<2 or isLongestPalindrome[j+1][i-1]):
                    isLongestPalindrome[0][j][i] = 1
                    if maxLen < i-j+1:
                        startIndex = j
                        endIndex = i+1
                        maxLen = i-j+1
                j -= 1
        return s[startIndex:endIndex]


if __name__ == '__main__':
    s = 'abcdcba'

    solver = Solution2()
    print(solver.longestPalindrome(s))
