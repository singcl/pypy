# coding: utf-8

"""Python 元组.

Python 元组详细描述docstrings.
元组封装和序列拆封.
"""

t = 1234, True, 'hello'
print t[0]
print t

# Tuples may be nested
u = t, (1, 2, 3, 4, 5)
print u

# Tuples are immutable:
# t[0] = 88888
# Traceback(most recent call last):
#   File "c:\Users\singcl.000\Desktop\pypy\tuple.py", line 18, in < module >
#     t[0] = 88888
# TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print v

# 空元组
empty = ()
singleton = 'hello',    # <-- note trailing comma
print singleton

# 元组封装和序列拆封
x, y, z = t
