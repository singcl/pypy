#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Python 并发下载
通俗的说就是让生成器执行到有yield关键字的地方挂起，
当然也可以通过next(consumer)来达到同样的效果。
如果不愿意每次都用这样的代码来“预激”生成器，可以写一个包装器来完成该操作，代码如下所示。

Version: 0.1
Author: singcl
Date: 2019-5-17
"""
from functools import wraps


def coroutine(fn):
    def wrapper(*args, **kwargs):
        gen = fn(*args, **kwargs)
        next(gen)
        return gen
    return wrapper
