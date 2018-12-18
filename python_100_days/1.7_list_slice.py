#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 和字符串一样，列表也可以做切片操作
通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表，
如何定义列表、使用下标访问列表元素以及添加和删除元素的操作。

Version: 0.1
Author: singcl
Date: 2018-12-19

"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=" ")
    print()

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)

    # fruit3 = fruits  # 没有复制列表只创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)

    fruits4 = fruits[-3:-1]
    print(fruits4)

    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    # :-2 表示步长为-2
    fruits5 = fruits[::-2]
    print(fruits5)


if __name__ == "__main__":
    main()
