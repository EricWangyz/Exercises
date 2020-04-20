#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 17:10
# @Author  : Eric Wang
# @File    : 舞蹈早晚课程0906.py


def perfectDancer(countMorning, countEvening, morningList, eveningList):
    commonID = []
    for i in morningList:
        if i in eveningList:
            commonID.append(i)

    for j in commonID:
        while j in eveningList:
            eveningList.remove(j)
        while j in morningList:
            morningList.remove(j)

    return len(morningList + eveningList)


if __name__ == "__main__":
    countMorning = 11
    countEvening = 10
    morningList = [1, 1, 2, 3, 4, 5, 5, 7, 6, 9, 10]
    eveningList = [11, 12, 13, 4, 5, 6, 7, 18, 19, 20]

    print(perfectDancer(countEvening, countMorning, morningList, eveningList))
