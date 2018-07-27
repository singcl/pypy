# coding: utf-8

"""简单模块示例。

Python fibo模块
"""
print __name__


def fibo(n):
    """fibonacci基本原理"""
    a, b = 0, 1
    while b < n:
        a, b = b, a + b


def fibo2(n):
    """fibonacci返回list"""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


# Python 模块作为脚本执行示例.
# import fibo 不会执行这段代码
if __name__ == "__main__":
    import sys
    x = fibo2(int(sys.argv[1]))
    print x
