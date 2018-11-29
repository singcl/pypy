#!usr/bin/python
# -*- coding: utf-8 -*-

"""

求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

算法 - 穷举法

Version: 0.1
Author: singcl
Date: 2018-11-29

"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print("G: %d, M: %d, X: %d" % (x, y, z))
