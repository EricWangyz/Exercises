#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 14:18
# @Author  : Eric Wang
# @File    : 字符串列表按需输出0909.py


def wordOutput(numsWord, wordsList, numsMethod, methodsList):

    result = []
    for i in methodsList:
        if i == 1:
            result.append(maxWord(wordsList))

        elif i == 2:
            result.append(minWord(wordsList))

        elif i == 3:
            result.append(secondMaxWord(wordsList))

        elif i == 4:
            result.append(secondMinWord(wordsList))

        elif i == 5:
            result.append(reversedMaxWord(wordsList))

    return result


def maxWord(wordsList):
    chr2num = []
    for word in wordsList:
        chr2num.append(ord(word[0]))
    maxIdx = chr2num.index(max(chr2num))
    return wordsList[maxIdx]


def minWord(wordsList):
    chr2num = []
    for word in wordsList:
        chr2num.append(ord(word[0]))
    minIdx = chr2num.index(min(chr2num))
    return wordsList[minIdx]


def secondMaxWord(wordsList):
    chr2num = []
    for word in wordsList:
        chr2num.append(ord(word[0]))
    maxIdx = chr2num.index(max(chr2num))
    chr2num[maxIdx] = 0
    secondMaxIdx = chr2num.index(max(chr2num))
    return wordsList[secondMaxIdx]


def secondMinWord(wordsList):
    chr2num = []
    for word in wordsList:
        chr2num.append(ord(word[0]))
    minIdx = chr2num.index(min(chr2num))
    chr2num[minIdx] = len(wordsList) + 2
    secondMinIdx = chr2num.index(min(chr2num))
    return wordsList[secondMinIdx]


def reversedMaxWord(wordsList):
    newWordsList = []
    for word in wordsList:
        newWordsList.append(word[::-1])

    chr2num = []
    for word in newWordsList:
        chr2num.append(ord(word[0]))
    maxIdx = newWordsList.index(max(chr2num))
    return newWordsList[maxIdx]


if __name__ == '__main__':
    numsWord = 3
    wordsList = ['abc','def','bfg']
    numsMethod = 3
    methodsList = [1,2,3,4,5]

    print(wordOutput(numsWord,wordsList,numsMethod, methodsList))
