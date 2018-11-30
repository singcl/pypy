#!usr/bin/python
# -*- coding: utf-8 -*-

"""

找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: singcl
Date: 2018-11-30

"""

for num in range(100, 1000):
    low = num % 10
    min = num // 10 % 10
    heigh = num // 100

    if num == low ** 3 + min ** 3 + heigh ** 3:
        print(num)
