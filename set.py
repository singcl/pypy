# coding: utf-8

"""Python 集合 set.

set 集合代表 无序不重复元素集合。
"""
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit

print 'orange' in fruit
print 'crabgrass' in fruit

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print a
print b
print a - b
print a | b
print a & b
print a ^ b

# 集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print '集合推导结果：', a
print {'r', 'd'}
