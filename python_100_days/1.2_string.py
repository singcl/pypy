#!usr/bin/python
# -*- coding: utf-8 -*-

"""
字符串常用操作

Version: 0.1
Author: Singcl
Date: 2018-11-26

"""

str1 = 'hello world'
print("字符串的长度是：", len(str1))
print("单词的首字母大写：", str1.title())
print("字符串变大写：", str1.upper())
print("字符串是不是大写：", str1.isupper())
print("字符串是不是以hello开头:", str1.startswith('hello'))
print("字符串是不是以hello结尾:", str1.endswith('hello'))

str2 = '- \u9a81\u650a'
str3 = str1.title() + ' ' + str2.lower()

print(str3)
