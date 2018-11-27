#!usr/bin/python
# -*- coding: utf-8 -*-

"""

用户身份验证

Version: 0.1
Author: singcl
Date: 2018-11-27

"""

# import getpass
# from getpass import getpass
# from getpass import *

username = input("请输入用户名：")
password = input("请输入密码：")

# 输入口令的时候终端中没有回显
# password = getpass.getpass('请输入口令: ')

if username == "admin" and password == "123456":
    print("身份校验成功！")
else:
    print("身份校验失败！")
