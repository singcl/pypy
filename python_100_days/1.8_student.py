#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 类的定义和使用

Version: 0.1
Author: singcl
Date: 2019-01-05

"""


class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
        # 通过这个方法我们可以为学生对象绑定name和age两个属性
    # 类似js 类的constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s" % (self.name, course_name))

        # PEP 8要求标识符的名字用全小写多个单词用下划线连接
        # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print("%s正在观看爱情动作片" % self.name)


def main():
    student1 = Student('singcl', 28)
    student1.study("Go程序设计")
    student1.watch_av()
    student2 = Student('jingmi', 16)
    student2.study("线性代数")
    student2.watch_av()


if __name__ == "__main__":
    main()
