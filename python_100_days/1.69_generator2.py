#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Python 并发下载
生成器还可以叠加来组成生成器管道

Version: 0.1
Author: singcl
Date: 2019-5-16
"""
from time import sleep


# Fibonacci数生成器


def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

# 偶数生成器


def even(gen):
    for val in gen:
        if val % 2 == 0:
            yield val


def main():
    gen = even(fib())
    for _ in range(10):
        print(next(gen))


if __name__ == "__main__":
    main()
