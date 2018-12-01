#!usr/bin/python
# -*- coding: utf-8 -*-

"""
函数的定义和使用 - 计算组合数C(7,3)

Version: 0.1
Author: singcl
Date: 2018-12-01

"""


def factorial(n):
    """
    定义一个阶乘函数
    :param n: 非负整数
    :return result: n的阶乘
    """

    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


# 输出组合数C(7, 3)
print("输出组合数C(7, 3) = %d" % (factorial(7) // (factorial(3) * factorial(4))))
