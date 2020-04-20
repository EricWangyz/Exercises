#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/4/7 14:58   
# @Author  : Eric Wang         
# @File    : 因式分解.py        


def main():
    """
    用户键盘输入一个小于1000的整数，对其进行因式分解
    :return:
    """
    num_str = input('input a number(2<= num < 1000):')
    num = int(num_str)
    line = list()
    if num > 1000 or num <= 2:
        print("输入不合法")
    else:
        for i in range(2, num+1):
            while True:
                if num % i == 0:
                    line.append(i)
                    num = num / i
                else:
                    break

    line_str = list()
    for i in line:
        line_str.append(str(i))
    print(num_str + '=' + '*'.join(line_str))


if __name__ == '__main__':
    main()
