#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
华氏温度转换为摄氏温度计

F = 1.8C + 32

Version: 0.1
Author: Singcl
Date: 2018-11-26

"""

f = float(input("请输入华氏温度："))
c = (f - 32) / 1.8
print("%.1f华氏温度 = %.1f摄氏温度" % (f, c))
