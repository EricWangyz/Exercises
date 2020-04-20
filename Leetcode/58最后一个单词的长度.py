#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 22:15
# @Author  : Eric Wang
# @File    : 58最后一个单词的长度.py


class Solution:

    def lengthOfLastWord(self, s: str) -> int:

        word_list = s.split(" ")

        for sub_s in word_list[::-1]:
            if sub_s is not "":
                return len(sub_s)
        return 0


if __name__ == "__main__":
    str_list = ["a ", "b a     ", "", "hello world"]

    solver = Solution()

    for s in str_list:
        print(solver.lengthOfLastWord(s))
