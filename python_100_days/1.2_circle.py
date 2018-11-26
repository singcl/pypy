#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
输入半径计算圆的周长和面积

Version: 0.1
Author: Singcl
Date: 2018-11-26

"""

import math

radius = float(input("请输入圆的半径："))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius

print("圆的周长：%.2f" % perimeter)
print("圆的面积：%.2f" % area)
