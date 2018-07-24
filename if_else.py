# -*- coding: UTF-8 -*- 或者 #coding=utf-8 或者#coding:utf 都行
# coding:utf-8

""""if else 流程控制"""

x = int(raw_input(u"请输入一个整数:"))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
