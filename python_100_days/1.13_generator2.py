#!usr/bin/python
# -*- coding: utf-8 -*-

"""
生成器 - 生成器语法
创建生成器对象： 1. 元祖推导式  2.生成器函数
Version: 0.1
Author: singcl
Date: 2019-3-18
"""


def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1


for x in fib(20):
    print(x)
