#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 生成器函数

Version: 0.1
Author: singcl
Date: 2019-01-02

"""


def main():
    f = [1, 1]
    for i in range(2, 20):
        f += [f[i - 1] + f[i - 2]]
        # f.append(f[i - 1] + f[i -2])

    for val in f:
        print(val, end=' ')


if __name__ == '__main__':
    main()
