#!usr/bin/python
# -*- coding: utf-8 -*-

"""

掷骰子决定做什么事

Version: 0.1
Author: singcl
Date: 2018-11-27

"""

from random import randint

face = randint(1, 6)

if face == 1:
    result = "唱首歌"
elif face == 2:
    result = "跳个舞"
elif face == 3:
    result = "学狗叫"
elif face == 4:
    result = "做俯卧撑"
elif face == 5:
    result = "绕口令"
else:
    result = "真心话大冒险"

print(result)
