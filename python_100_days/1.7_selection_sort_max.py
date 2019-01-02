#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 找出列表中最大或最小的元素

Version: 0.1
Author: singcl
Date: 2019-01-02

"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    # 直接使用内置的max和min函数找出列表中最大和最小元素
    # print(max(fruits))
    # print(min(fruits))

    max_value = min_value = fruits[0]

    # 选择排序中的一个环节也是这样
    # https://github.com/singcl/playground/tree/master/c/c_sort
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]

    print("Max:", max_value)
    print("Min:", min_value)


if __name__ == '__main__':
    main()
