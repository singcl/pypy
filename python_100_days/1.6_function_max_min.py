#!usr/bin/python
# -*- coding: utf-8 -*-

"""
函数的定义和使用 - 求最大公约数和最小公倍数

Version: 0.1
Author: singcl
Date: 2018-12-02

"""

a = int(input("请输入非负整数a = "))
b = int(input("请输入非负整数b = "))


def gcd(x, y):
    """
    求最大公约数函数
    :param x: 非负整数
    :param y: 非负整数
    :return result: 非负整数
    """

    if x > y:
        (x, y) = (y, x)

    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

    return 1


def lcm(x, y):
    """
    求最小公倍数函数
    :param x: 非负整数
    :param y: 非负整数
    :return result: 非负整数
    """
    return x * y // gcd(x, y)


print("最大公约数：%d" % gcd(a, b))
print("最小公倍数：%d" % lcm(a, b))
