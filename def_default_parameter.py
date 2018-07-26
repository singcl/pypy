# coding: utf-8
"""函数默认参数"""


def ask_ok(prompt, reties=4, complaint="Yes or No, Please"):
    """函数默认参数的使用"""
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ("n", "no", "nop", "nope"):
            return False
        reties = reties - 1
        if reties < 0:
            raise IOError('refusenik user')
        print complaint


ask_ok('Do you really want to quit?')


# 默认值在函数的作用域内解析
i = 5


def foo(arg=i):
    """默认值在函数的作用域内解析"""
    print arg


i = 6
foo()

# 重要警告: 默认值只被赋值一次。这使得当默认值是可变对象时会有所不同


def bar(a, list=[]):
    """重要警告: 默认值只被赋值一次。这使得当默认值是可变对象时会有所不同"""
    list.append(a)
    return list


print bar(1)
print bar(2)
print bar(3)
