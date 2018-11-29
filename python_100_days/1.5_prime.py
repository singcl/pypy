#!usr/bin/python
# -*- coding: utf-8 -*-

"""

输出2~100之间的素数

Version: 0.1
Author: singcl
Date: 2018-11-30

"""

import math

for x in range(2, 100 + 1):
    is_prime = True
    # for y in range(2, x // 2 + 1):
    for y in range(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            is_prime = False
            break
    if is_prime:
        print(x, end=" ")
