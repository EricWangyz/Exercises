#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/7/27 21:52   
# @Author  : Eric Wang         
# @File    : 正则表达式匹配.py        

class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        # 若字符串和匹配模式长度均为0，则可以匹配
        if len(s) == 0 and len(p) == 0:
            return True
        # 若字符串长度不为0，而字符模式为0，则不匹配
        if len(s) > 0 and len(p) == 0:
            return False
        # 若匹配模式长度大于1，并且匹配模式的第一个符号为‘*’，则对字符串进行判断
        if len(p) > 1 and p[1] == '*':
            # 如果字符串长度大于0且字符串与匹配模式的第一个字符相同，或者匹配模式的第一个符号为‘.’
            # 则
            if len(s) > 0 and (s[0] == p[0] or p[0] =='.'):
                return self.isMatch(s, p[2:]) or \
                       self.isMatch(s[1:], p[2:]) or \
                       self.isMatch(s[1:], p)  #
            else:
                return self.isMatch(s, p[2:])
        # 字符串第长度大于0，且与匹配模式的第一个符号相同，或者匹配模式的第一个符号为‘.’，
        # 则继续进行后面的匹配
        if len(s) > 0 and (p[0] == '.' or p[0] == s[0]):
            return self.isMatch(s[1:], p[1:])
        return False


class Solution2:
    # s, pattern都是字符串
    def isMatch(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.isMatch(s, pattern[2:]) or \
                       self.isMatch(s[1:], pattern[2:]) or \
                       self.isMatch(s[1:], pattern)
            else:
                return self.isMatch(s, pattern[2:])
        if len(s) > 0 and (pattern[0] == '.' or pattern[0] == s[0]):
            return self.isMatch(s[1:], pattern[1:])
        return False


class Solution3(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


if __name__ == '__main__':
    s = "aaaaaaaaaaaaab"
    p = "a*a*a*a*a*a*a*a*a*a*c"

    solver = Solution3()
    print(solver.isMatch(s,p))