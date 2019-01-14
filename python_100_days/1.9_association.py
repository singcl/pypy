#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 对象之间的关联关系

Version: 0.1
Author: singcl
Date: 2019-01-14

"""

from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def move_to(self, x, y):
        self._x = y
        self._y = y

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy

    def distance_to(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return "(%s, %s)" % (str(self._x), str(self._y))


if __name__ == "__main__":
    p1 = Point(3, 5)
    print(p1)
    p2 = Point(-2, -1.5)
    print(p2)
    print(p1.distance_to(p2))

