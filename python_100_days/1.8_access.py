#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 类的定义和使用
前置双下划线定义类的私有方法和属性

Version: 0.1
Author: singcl
Date: 2019-01-08
"""

class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    test = Test("hello")
    test._Test__bar() # 访问私有方法
    print(test._Test__foo) # 访问私有属性

if __name__ == "__main__":
    main()
