#!usr/bin/python
# -*- coding: utf-8 -*-

"""

用while循环实现1~100 偶数求和

Version: 0.1
Author: singcl
Date: 2018-11-28

"""
sum = 0
num = 1

while num <= 100:
    if num % 2 == 0:
        sum += num

    num += 1

print(sum)


# 第二种
sum2 = 0
num2 = 2

while num2 <= 100:
    sum2 += num2
    num2 += 2

print(sum2)
