#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 类的定义和使用
另一种创建类的方式

Version: 0.1
Author: singcl
Date: 2019-01-08
"""

def bar(self, name):
    self._name = name


def foo(self, course_name):
    print("%s正在学习%s" % (self._name, course_name))

def main():
    Student = type("Student", (object,), dict(__init__ = bar, study=foo))
    stu1 = Student("singcl")
    stu1.study("Python")


if __name__ == "__main__":
    main()
