#!usr/bin/python
# -*- coding: utf-8 -*-

"""

输入非负整数n计算n!

Version: 0.1
Author: singcl
Date: 2018-11-28

"""
n = int(input("n = "))

result = 1
for x in range(1, n + 1):
    result = result * x

print("%d! = %d" % (n, result))
