#!usr/bin/python
# -*- coding: utf-8 -*-

"""

九九乘法

Version: 0.1
Author: singcl
Date: 2018-11-29

"""

for x in range(1, 10):
    for y in range(1, x + 1):
        print("%d x %d = %d" % (y, x, y * x), end="\t")
    print()
