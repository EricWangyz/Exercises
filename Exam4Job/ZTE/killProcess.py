#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/9/9 19:56   
# @Author  : Eric Wang         
# @File    : killProcess.py        

class Solution(object):
    def killProcess(self, pid, ppid, kill):

        dict1 = {}
        size = len(pid)
        res = [kill]
        for i in range(size):
            if dict1.get(ppid[i]) == None:
                dict1[ppid[i]] = [pid[i]]
            else:
                dict1[ppid[i]] += [pid[i]]
        kill = [kill]
        while kill != []:
            tmp = kill[0]
            if dict1.get(tmp) != None:
                res += dict1[tmp]
                kill += dict1[tmp]
            del kill[0]
        return len(res)


if __name__ == '__main__':
    solution = Solution()

    pid = [3,1,5,21,10]
    ppid = [0,3,3,1,5]
    kill = 5

    print(solution.killProcess(pid, ppid, kill))