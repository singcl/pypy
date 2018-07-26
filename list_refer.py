# coding: utf-8

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]

[-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
[0, 2, 4]
# apply a function to all the elements
[abs(x) for x in vec]
[4, 2, 0, 2, 4]
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# the tuple must be parenthesized, otherwise an error is raised
# [x, x**2 for x in range(6)]
#   File "<stdin>", line 1, in ?
#     [x, x**2 for x in range(6)]
#                ^
# SyntaxError: invalid syntax
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

from math import pi
print [str(round(pi, i)) for i in range(6)]

# 3 x 4 矩阵列表推导
matrix = [
    [1, 4, 7, 10],
    [2, 5, 8, 11],
    [3, 6, 9, 12]
]
print [[row[i] for row in matrix] for i in range(4)]

# 在实际中，你应该更喜欢使用内置函数组成复杂流程语句。对此种情况 zip() 函数将会做的更好:
print list(zip(*matrix))
