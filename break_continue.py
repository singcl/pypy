# coding=utf-8

""""
Python 之 break continue
break 语句和 C 中的类似，用于跳出最近的一级 for 或 while 循环。
循环可以有一个 else 子句；它在循环迭代完整个列表 (对于 for) 后或执行条件为 false (对于 while) 时执行.
但循环被 break 中止的情况下不会执行。以下搜索素数的示例程序演示了这个子句:
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'

# W: 14, 4: Else clause on loop without a break statement (useless-else-on-loop)
