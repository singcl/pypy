#!usr/bin/python
# -*- coding: utf-8 -*-

"""

分制成绩转等级制成绩

90分以上 	 	--> A
80分~89分 	    --> B
70分~79分	    --> C
60分~69分	    --> D
60分以下		--> E

Version: 0.1
Author: singcl
Date: 2018-11-27

"""

score = float(input("请输入成绩："))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"

"""
在if-elif-else、for-else、while、try-except\try-finally等关键字的语句块中并不会产成作用域。
类似js ES6之前没有块级作用域
"""
print("%.2f分对应的等级是：%s" % (score, grade))
