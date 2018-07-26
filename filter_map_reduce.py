# coding: utf-8

"""Python 函数式编程方法"""


def f(x): return x % 3 == 0 or x % 5 == 0


print 'filter:', filter(f, range(2, 25))
# print filter(lambda x: x % 3 == 0 or x % 5 == 0, range(2, 25))


def cube(x): return x*x*x


print map(cube, range(1, 11))


# map函数传入多个序列
seq = range(8)


def add(x, y): return x + y


print 'Map:', map(add, seq, seq)

# Reduce
print 'Reduce:', reduce(add, range(1, 11))

print 'sum:', sum(range(10))

# 列表推导
sequares = []
for x in range(10):
    sequares.append(x**2)
print sequares

sequares2 = [x**3 for x in range(10)]
print sequares2

print map(lambda x: x**3, range(10))

# 列表推导2
print [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
