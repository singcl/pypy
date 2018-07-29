# coding=utf-8

"""Python 字符串格式化的N种方法"""

import string

x = 'singcl'
print 'hehehe %s' % x

# 字符串模板
xx = string.Template('${x} ${h}shes guangzhou')
print xx.substitute({'x': 'singccl', 'h': 'hongkong'})
