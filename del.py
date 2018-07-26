# coding: utf-8

"""DEL语句

如何使用del语句
"""

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
print a
del a[2:4]
print a
del a[:]
print a
