#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python set集合数据结构
Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。

Version: 0.1
Author: singcl
Date: 2018-12-25

"""


def main():
    # 数学上集合也是这么写的
    set1 = {1, 2, 3, 3, 3, 3, 2}
    print(set1)
    print("Length = ", len(set1))

    set2 = set(range(1, 10))
    print(set2)

    set1.add(4)
    set1.add(5)
    set2.update([11, 12])

    print(set1)
    print(set2)

    set2.discard(5)
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)

    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=" ")
    print()

    set3 = set((12, 3, 4, 5, 5, 43, 3))
    print(set3)

    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    # print(set1.intersection(set2))
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))

    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))


if __name__ == "__main__":
    main()
