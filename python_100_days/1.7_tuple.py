#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 元组的定义和使用

Version: 0.1
Author: singcl
Date: 2019-01-04

"""
def main():
    # 定义元组
	t = ('jim', 38, True, 'joho')
	print(t)
	# 获取元组中的元素
	print(t[0])
	print(t[1])
	print(t[2])
	print(t[3])
	# 遍历元组中的值
	for member in t:
		print(member)
	# 重新给元组赋值
	# t[0] = 'tom'		# TypeError
	# 变量t重新引用了新的元组 原来的元组被垃圾回收
	t = ('tom', 20, True, 'hax')
	print(t)
	# 元组和列表的转换
	person = list(t)
	print(person)
	person[0] = 'tom'
	person[1] = 25
	print(person)
	fruits_list = ['apple', 'banana', 'orange']
	fruits_tuple = tuple(fruits_list)
	print(fruits_tuple)
	print(fruits_tuple[1])


if __name__ == '__main__':
	main()
