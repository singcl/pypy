#!usr/bin/python
# -*- coding: utf-8 -*-

"""
读取CSV数据
Version: 0.1
Author: singcl
Date: 2019-01-31
"""


import csv


class Teacher(object):
    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def title(self):
        return self.__title


filename = 'teacher.csv'
teachers = [Teacher('Tom', 32, '高级前端开发'), Teacher('singcl', 22, '资深前端开发')]

try:
    with open(filename, 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writerow([teacher.name, teacher.age, teacher.title])
except BaseException as e:
    print("无法写入文件", filename)
else:
    print('保存数据成功！')
