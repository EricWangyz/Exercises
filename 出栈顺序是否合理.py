#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/5/27 22:50   
# @Author  : Eric Wang         
# @File    : 出栈顺序是否合理.py        

'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该
压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）

解题思路
1.我们申请一个的新的列表stack，依次将入栈序列中的值加入
2.每次加入stack,我们需要将stack的顶部的数和出栈序列中起始index的数做对比，
如果相等，我们将stack中的顶部弹出，并且出栈序列的index依次后移，重复这样的操作，
直到值不相等或者出栈序列已经空了为止
3.最后，我们检验stack中是否为空，如果为空，则入栈和出栈序列是合理的，否则不是合理的

'''


import sys

def is_pop_order(pushV, popV):
    # 判断入栈序列长度是否为0，0则返回错误
    if len(pushV) == 0:
        return False
    stack = []
    j = 0
    for i in range(len(pushV)):
        stack.append(pushV[i])
        # 依次按照入栈序列将元素压入栈中，
        # 当发现栈顶元素与当前弹出序列的首元素相同时，弹出该元素，
        # 之后删除弹出序列中在stack中已经弹出的元素
        while j < len(popV) and stack[-1] == popV[j]:
            stack.pop()
            j += 1 # j相当于弹出序列的指针，弹出一个，删除一个，等效操作就是依次往后移动一位
    if len(stack) == 0: # 直到stack出战完全，即长度为0时，表明出栈序列符合
        return True
    else:
        return False


def main():
    p_push = sys.stdin.readline().strip()
    p_stack = sys.stdin.readline().strip()

    print(is_pop_order(p_push, p_stack))


if __name__ == '__main__':
    main()