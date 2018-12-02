#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python的内置函数
	- 数学相关: abs / divmod / pow / round / min / max / sum
	- 序列相关: len / range / next / filter / map / sorted / slice / reversed
	- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
	- 数据结构: dict / list / set / tuple
	- 其他函数: all / any / id / input / open / print / type

Version: 0.1
Author: singcl
Date: 2018-12-02

"""
def myfilter(mystr):
    return len(mystr) == 6

# help()
print(chr(0x5fb7)) # 十进制或者十六进制数转对应的字符串
print(hex(ord("德"))) # ord返回字符的十进制码点 hex 十进制转十六进制数
print(abs(-1.2345)) # abs绝对值
print(pow(2,4)) # 2的4次方
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])
fruits2 = list(filter(myfilter, fruits))
print(fruits)
print(fruits2)
