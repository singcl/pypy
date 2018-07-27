# coding: utf-8

"""Python 写文件

写文件啦
"""

f = open('read_file.py', 'wb')
f.write('#文件被重写啦')

t = ('the answer', 42)
s = str(t)
f.write(s)

with open('range.py', 'r') as ff:
    read_data = ff.read()
print ff.closed

# 使用 json 存储结构化数据