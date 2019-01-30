#!usr/bin/python
# -*- coding: utf-8 -*-

"""
读取CSV数据
Version: 0.1
Author: singcl
Date: 2019-01-30
"""

import csv

filename = 'example.csv'

try:
    with open(filename) as f:
        reader = csv.reader(f)
        data = list(reader)
except FileNotFoundError:
    print("无法打开文件", filename)
else:
    for item in data:
        print("%-30s%-20s%-10s" % (item[0], item[1], item[2]))
