#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
第一个Python程序
问候世界

Version: 0.1
Author: singcl
Date: 2018-11-25

请将该文件命名为hello.py并在终端中通过下面的命令运行它
python hello.py
"""

# print 基本用法
print("hello world!")
print("您好", "中国")
print('hello', 'world', sep=',', end='!')
print('goodbye', 'world', end='!\n')

# print 格式化输出用法
# % 来格式化输出
print('%d - %s - %.2f' % (3333, 'singcl', 33.232322))
# 利用format来格式化定义
print("I am {}".format('Sin'))
print('this is {1} {0}'.format('apple', 'an'))
print('this is {number} {fruit}'.format(number='an', fruit='apple'))
# 3.x才能使用的语法f-string寓意快速
temp = "Sin2"
print(f"I am {temp}")
