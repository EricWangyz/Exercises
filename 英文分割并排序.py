#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/7 16:33   
# @Author  : Eric Wang         
# @File    : 英文分割并排序.py

"""
输入一个英文句子，把句子中的单词(不区分大小写)按出现次数按从多到少
把单词和次数在屏幕上输出来，要求能识别英文句号和逗号，
即是说单词由空格、句号和逗号隔开。
"""
try:
    while True:
        dict_sent = {}
        string = input()
        string = string.replace(',',' ').replace('.',' ')
        string = string.lower()
        string = string.split()
        string.sort()
        for item in string:
            dict_sent[item] = dict_sent.get(item, 0) + 1
        print(dict_sent)
        print(dict_sent.items())
        dict_sent = sorted(dict_sent.items())
        print(dict_sent)
        # for i in dict_sent:
        #     print('%s:%s' % i)
except:
    pass

