#!usr/bin/python
# -*- coding: utf-8 -*-

"""

定义和使用列表
	- 用下标访问元素
	- 添加元素
	- 删除元素

Version: 0.1
Author: singcl
Date: 2018-12-26

"""


def main():
    fruits = ['grape', '@pple', 'strawberry', 'waxberry']
    print(fruits)

    # 通过下标访问元素
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])
    # print(fruits[-5])  # IndexError: list index out of range

    fruits[1] = "apple"
    print(fruits)

    # 添加元素
    fruits.append('banana')
    fruits.insert(0, 'pear')
    print(fruits)

    # 删除元素
    del fruits[1]
    fruits.pop()
    fruits.pop(0)
    fruits.remove('apple')
    print(fruits)


if __name__ == "__main__":
    main()
