#!usr/bin/python
# -*- coding: utf-8 -*-

"""
函数的参数
	- 默认参数
	- 可变参数
	- 关键字参数
	- 命名关键字参数

Version: 0.1
Author: singcl
Date: 2018-12-03

"""
# 参数默认值


def f1(a, b=5, c=10):
    return a + b * 2 + c*3


print(f1(1, 2, 3))
print(f1(100, 100))
print(f1(100))
print(f1(c=2, b=3, a=10))

# 可变参数


def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(f2(1, 2, 3))
print(f2(1, 2, 3, 4, 5))
print(f2())


# 关键字参数
def f3(**kwargs):
    if 'name' in kwargs:
        print("欢迎您%s" % kwargs['name'])
    elif 'tel' in kwargs:
        print('你的联系电话是: %s!' % kwargs['tel'])
    else:
        print('没找到你的个人信息!')


param = {'name': 'Singcl', 'age': 16}
f3(**param)

f3(name='singcl', age=14, tel='15881521256')
f3(user='singcl', age=14, tel='15881521256')
f3(user='singcl', age=14, mobile='15881521256')
