#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
格式化输出

Version: 0.1
Author: Singcl
Date: 2018-11-26

"""

a = int(input("a = "))
b = int(input("b = "))

print("%d + %d = %d" % (a, b, a + b))
print("%d - %d = %d" % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
