#!usr/bin/python
# -*- coding: utf-8 -*-

"""

斐波那契数列

Version: 0.1
Author: singcl
Date: 2018-11-30

"""

a = 0
b = 1

for _ in range(20):
    (a, b) = (b, a + b)
    print(a, end=' ')

