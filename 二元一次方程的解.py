#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/29 20:39   
# @Author  : Eric Wang         
# @File    : 二元一次方程的解.py        

import sys
from math import sqrt


class solution(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


    def getResult(self):
        # print "type b ",self.b,type(self.b)
        # print "type a",self.a,type(self.a)
        if self.a == 0:
            print("x=%.2f" % (-self.c*1.0/self.b))
        elif self.b*self.b - 4*self.a*self.c < 0:
            print(-1)
        elif self.b*self.b - 4*self.a*self.c == 0:
            # 这里莫名其妙踩了个大坑, -self.b先被当成参数弄进了字符串,加个括号才行
            # TypeError: unsupported operand type(s) for /: 'str' and 'int'
            print("x=%.2f" % ((-self.b+0.0)/self.a/2.0))
        else:
            print("x1=%.2f,x2=%.2f" %
                  ((-self.b-sqrt(self.b*self.b - 4*self.a*self.c))/self.a/2.0,
                   (-self.b+sqrt(self.b*self.b - 4*self.a*self.c))/self.a/2.0))


if __name__ == "__main__":
    m = int(sys.stdin.readline().strip())
    N = []
    for i in range(m):
        N.append(sys.stdin.readline().strip().split())
    for n in N:
        a,b,c = int(n[0]),int(n[1]),int(n[2])
        # print type(a),type(b),type(c)
        solution(a,b,c).getResult()
