#!usr/bin/python
# -*- coding: utf-8 -*-

"""

用for循环实现1~100 偶数求和

Version: 0.1
Author: singcl
Date: 2018-11-28

"""
sum = 0

for x in range(2, 101, 2):
    sum += x

print(sum)
