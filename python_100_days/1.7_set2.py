#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python set集合数据结构
Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。
集合的常用操作
	- 交集
	- 并集
	- 差集
	- 子集
	- 超集

Version: 0.1
Author: singcl
Date: 2019-01-01

"""


def main():
    set1 = set(range(1, 10))
    print(set1)
    set2 = set(range(1, 10, 2))
    print(set2)
    set3 = set(range(1, 6))

    # print(set1.intersection(set2))
    print(set1 & set3)
    # print(set1.union(set2))
    print(set1 | set2)
    # print(set1.difference(set2))
    print(set1 - set2)
    # print(set1.symmetric_difference(set2))
    print(set1 ^ set2)
    # print(set2.issubset(set1))
    print(set2 <= set1)
    # print(set3.issubset(set1))
    print(set3 <= set1)
    # print(set1.issuperset(set2))
    print(set1 >= set2)
    # print(set1.issuperset(set3))
    print(set1 >= set3)


if __name__ == "__main__":
    main()
