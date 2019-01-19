#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 对象之间的依赖关系和运算符重载

Version: 0.1
Author: singcl
Date: 2019-01-19

"""


class Car(object):
    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand

    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%s当时时速%d' % (self._brand, self._current_speed)


class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # 学生和车之间存在依赖关系 - 学生使用了汽车
    def drive(self, car):
        print("%s驾驶着%s欢快的行驶在去西天的路上" % (self._name, car._brand))
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        car.accelerate(50)
        print(car)

    def study(self, course_name):
        print("%s正在学习%s." % (self._name, course_name))

    def watch_tv(self):
        if self._age < 18:
            print('%s只能观看《熊出没》.' % self._name)
        else:
            print('%s正在观看岛国爱情动作片.' % self._name)

    # 重载大于(>)运算符
    def __gt__(self, other):
        return self._age > other._age

    # 重载小于(<)运算符
    def __lt__(self, other):
        return self._age < other._age


if __name__ == "__main__":
    student1 = Student('singcl', 22)
    student1.study('Python 100天')
    student1.watch_tv()

    student2 = Student('jingmiao', 15)
    student2.study("思想品德")
    student2.watch_tv()

    car = Car('BMW', 120)
    student1.drive(car)

    # 运算符重载
    print(student1 > student2)
    print(student1 < student2)
