# coding: utf-8

"""格式化输出

Python之格式化输出
"""

s = 'Hello world'
print str(s)
print repr(s)

print str(1/7)

# 有两种方式可以写平方和立方表:
for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),
    print repr(x*x*x).rjust(4)

for x in range(1, 11):
    print '{0:2d} {1: 3d} {2: 4d}'.format(x, x*x, x**3)
