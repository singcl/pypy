#!/usr/bin/python
# -*- codeing: utf-8 -*-

"""
Python 装饰器
基于类的装饰器

__call__其他作用
实例对象也可以像函数一样作为可调用对象来用，
那么，这个特点在什么场景用得上呢？
这个要结合类的特性来说，类可以记录数据（属性），而函数不行（闭包某种意义上也可行），
利用这种特性可以实现基于类的装饰器，在类里面记录状态，比如，下面这个例子用于记录函数被调用的次数

@see https://www.jianshu.com/p/e1d95c4e1697?utm_source=oschina-app

Version: 0.1
Author: Singcl
Date: 2019-5-19
"""


class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@Counter
def foo():
    pass


for _ in range(10):
    foo()

print(foo.count)  # 10
