# coding: utf-8
"""循环技巧.

Python 循环技巧。
"""
# 在序列中循环时，索引位置和对应值可以使用 enumerate() 函数同时得到:
for i, v in enumerate(['tic', 'tac', 'toe']):
    print (i, v),

# 同时循环两个或更多的序列，可以使用 zip() 整体打包:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)

# 需要逆向循环序列的话，先正向定位序列，然后调用 reversed() 函数:
for i in reversed(xrange(1, 10, 2)):
    print (i)

# 要按排序后的顺序循环序列的话，使用 sorted() 函数，它不改动原序列，而是生成一个新的已排序的序列:
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print f

# 遍历字典时，使用 iteritems() 方法可以同时得到键和对应的值。:
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print (k, v)

# 若要在循环内部修改正在遍历的序列（例如复制某些元素），建议您首先制作副本。在序列上循环不会隐式地创建副本。切片表示法使这尤其方便:
words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print words
