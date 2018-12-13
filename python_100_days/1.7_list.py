#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 如何定义列表、使用下标访问列表元素以及添加和删除元素的操作。

Version: 0.1
Author: singcl
Date: 2018-12-13

"""


def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)

    list2 = ['hello'] * 5
    print(list2)

    # 计算列表长度(元素个数)
    print(len(list2))
    # 下标(索引)运算
    print(list1[0])
    print(list1[4])
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1])
    print(list1[-3])

    # 修改元素
    list1[2] = 300
    print(list1)

    # 添加元素
    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 3000]
    print(list1)
    print(len(list1))

    # 删除元素
    list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)

    del list1[0]
    print(list1)

    # 清空列表元素
    list1.clear()
    print(list1)


if __name__ == "__main__":
    main()
