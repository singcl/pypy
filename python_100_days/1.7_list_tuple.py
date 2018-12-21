#!usr/bin/python
# -*- coding: utf-8 -*-

"""

Python 的元组与列表类似，不同之处在于元组的元素不能修改

Version: 0.1
Author: singcl
Date: 2018-12-21

"""

def main():
    # 定义元祖
    t = ("singcl", 32, True, [43, 4])
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for x in t:
        print(x)

    # 重新给元组赋值
    # t[0] = 'hello' # TypeError: 'tuple' object does not support item assignment
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('word', 20, True, 'gul')
    print(t)
	# 将元组转换成列表
    p = list(t)
    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(p)


if __name__ == "__main__":
    main()
