#!usr/bin/python
# -*- coding: utf-8 -*-

"""

英制单位英寸和公制单位厘米互换

Version: 0.1
Author: singcl
Date: 2018-11-27

"""

value = float(input("请输入长度："))
unit = input("请输入单位：")

if unit == 'in' or unit == '英寸':
    print("%f英寸 = %f厘米" % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print("%f厘米 = %f英寸" % (value, value / 2.54))
else:
    print("请输入有效的单位")
