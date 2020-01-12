# -*-coding: utf-8 -*-
import time
import functools

"""
装饰器 - 时间统计
"""

def time_statistics(fun):
    # 值得注意的是@functools.wraps(func)，这是python提供的装饰器
    # 它能把原函数的元信息拷贝到装饰器里面的 func 函数中。
    # 函数的元信息包括docstring、name、参数列表等等
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = fun(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" %
              (fun.__name__, str(t1 - t0)))
        return result

    return wrapper
