"""
继承的应用
	- 抽象类
	- 抽象方法
	- 方法重写
	- 多态
Version: 0.1
Author: singcl
Date: 2019-01-19
"""

from abc import ABCMeta, abstractmethod
from math import pi


class Shape(object, metaclass=ABCMeta):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def perimeter(self):
        return 2 * pi * self._radius

    def area(self):
        return pi * self._radius ** 2

    def __str__(self):
        return "我是一个圆"


class Rect(Shape):

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def perimeter(self):
        return 2 * (self._width + self._length)

    def area(self):
        return self._width * self._length

    def __str__(self):
        return "我是个矩形"


if __name__ == "__main__":
    shapes = [Circle(5), Circle(3.2), Rect(3.2, 6.4)]
    for shape in shapes:
        print(shape)
        print("周长:", shape.perimeter())
        print("面积：", shape.area())
