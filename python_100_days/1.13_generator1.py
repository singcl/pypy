#!usr/bin/python
# -*- coding: utf-8 -*-

"""
生成器 - 生成器语法
创建生成器对象： 1. 元祖推导式  2.生成器函数
Version: 0.1
Author: singcl
Date: 2019-3-18
"""

# list直接生成结果
seq = [x * x for x in range(10)]
print(seq)

# 元祖生成的生成器对象，迭代时才计算
gen = (x * x for x in range(10))
print(gen)


for x in gen:
    print(x)

num = 10
gen = (x ** y for x, y in zip(range(1, num), range(num - 1, 0, -1)))
print(gen)

n = 1
while n < num:
    print(next(gen))
    n += 1
