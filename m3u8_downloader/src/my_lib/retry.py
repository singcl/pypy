
# -*-coding: utf-8 -*-
import functools

"""
装饰器 - 设置重试次数
"""
def retry(retries=3):
    def _retry(fun):
        # 值得注意的是@functools.wraps(func)，这是python提供的装饰器
        # 它能把原函数的元信息拷贝到装饰器里面的 func 函数中。
        # 函数的元信息包括docstring、name、参数列表等等
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return fun(*args, **kwargs)
                except Exception as e:
                    print("@", fun.__name__, "->", e)
        return wrapper
    return _retry
