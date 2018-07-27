# coding: utf-8
"""Python 字典.

另一个非常有用的 Python 内建数据类型是 字典 (参见 Mapping Types — dict )。
字典在某些语言中可能称为 联合内存 (associative memories) 或 联合数组 (associative arrays)。
序列是以连续的整数为索引，与此不同的是，字典以 关键字 为索引，关键字可以是任意不可变类型，通常用字符串或数值。
如果元组中只包含字符串和数字，它可以作为关键字，如果它直接或间接地包含了可变对象，就不能当做关键字。
不能用链表做关键字，因为链表可以用索引、切割或者 append() 和 extend() 等方法改变。
理解字典的最佳方式是把它看做无序的键：值对 (key:value 对)集合，键必须是互不相同的(在同一个字典之内)。
一对大括号创建一个空的字典：{}。初始化链表时，在大括号内放置一组逗号分隔的键：值对，这也是字典输出的方式。
字典的主要操作是依据键来存储和析取值。也可以用 del 来删除键：值对(key:value)。
如果你用一个已经存在的关键字存储值，以前为该关键字分配的值就会被遗忘。试图从一个不存在的键中取值会导致错误。
对一个字典执行 keys() 将返回一个字典中所有关键字组成的无序列表(如果你想要排序，只需使用 sorted())。
使用 in 关键字(指 Python 语法)可以检查字典中是否存在某个关键字(指字典)。
"""
tel = {'jack': 4098, 'sape': 4139}
print tel

print tel.keys()

print dict([('space', 321), ('guido', 4127), ('jack', 4098)])

# 字典推导式
print {x: x**2 for x in (2, 3, 4)}

# 如果关键字都是简单的字符串，有时通过关键字参数指定 key-value 对更为方便:
dict(space=322, guido=4127, jack=4098)