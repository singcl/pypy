#!usr/bin/python
# -*- coding: utf-8 -*-

"""

计算两个数的最大公约数和最小公倍数

Version: 0.1
Author: singcl
Date: 2018-11-28

"""
x = int(input("请输入一个正整数："))
y = int(input("请输入一个正整数："))

if x > y:
    (x, y) = (y, x)

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d的最大公约数是：%d" % (x, y, factor))
        print("%d和%d的最小公倍数：%d" % (x, y, x * y // factor))
        break
