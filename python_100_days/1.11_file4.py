#!usr/bin/python
# -*- coding: utf-8 -*-

"""
读写二进制文件
Version: 0.1
Author: singcl
Date: 2019-01-31
"""
import base64

with open('mm.png', 'rb') as f:
    data = f.read()
    # print(type(data))
    # print(data)
    print('字节数:', len(data))
    # 将图片处理成BASE-64编码
    print(base64.b64encode(data))

with open('girl.png', 'wb') as f:
    f.write(data)
print('写入完成!')
