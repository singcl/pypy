#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 生成器函数

Version: 0.1
Author: singcl
Date: 2018-12-21

"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def main():
    for val in fib(20):
        print(val)


if __name__ == "__main__":
    main()
