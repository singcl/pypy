# coding: utf-8

"""
"""


def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0 ,1
    while a < n:
        print a,
        a, b = b, a + b


fib(2000)
