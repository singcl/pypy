#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python字符串的使用

Version: 0.1
Author: singcl
Date: 2018-12-13

"""


def main():
    str1 = "hello world"
    # 通过len函数计算字符串的长度
    print(len(str1))
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())
    # 获得字符串变大写后的拷贝
    print(str1.upper())
    # 从字符串中查找子串所在位置
    print(str1.find('or'))
    print(str1.find('shit'))
    # 与find类似但找不到子串时会引发异常
    print(str1.index('or'))
    # print(str1.index('shit'))


if __name__ == '__main__':
    main()
