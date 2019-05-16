#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Python 并发下载
生成器 - 数据的生产者。

Version: 0.1
Author: singcl
Date: 2019-5-16
"""
from time import sleep

# 倒计数生成器


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def main():
    for num in countdown(5):
        print(f'Countdown: {num}')
        sleep(1)
    print('Countdown Over!')


if __name__ == "__main__":
    main()
