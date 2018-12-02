#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python常用模块
	- 运行时服务相关模块: copy / pickle / sys / ...
	- 数学相关模块: decimal / math / random / ...
	- 字符串处理模块: codecs / re / ...
	- 文件处理相关模块: shutil / gzip / ...
	- 操作系统服务相关模块: datetime / os / time / logging / io / ...
	- 进程和线程相关模块: multiprocessing / threading / queue
	- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
	- Web编程相关模块: cgi / webbrowser
	- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...

Version: 0.1
Author: singcl
Date: 2018-12-03

"""

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
# Pyhton 通知类来自定义数据类型
print(type(localtime))
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
print(localtime.tm_hour)
print(localtime.tm_min)
print(localtime.tm_sec)

asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print(strtime)
mydate = time.strptime("2018-1-1", "%Y-%m-%d")
print(mydate)

# copy
shutil.copy("./1.1_hello.py", "./shutil.txt")

# 调用系统命令ls -la
os.system('ls -la')
# 改变当前工作目录
os.chdir("../music")
# 再次调用系统命令ls -la
os.system('ls -l')
os.mkdir('x')
os.chdir('./x')
os.system("touch xx.txt")
