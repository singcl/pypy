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


# 关键字函数
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    """关键字参数的基本使用规则"""
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# 未出现在形式参数列表中的关键字参数
def cheeseshop(kind, *args, **kwargs):
    """未出现在形式参数列表中的关键字参数"""
    print '-' * 40
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in args:
        print arg
    print '-' * 40
    keys = sorted(kwargs.keys())
    for kw in keys:
        print kw, ":", kwargs[kw]


cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", shopkeeper='Michael Palin',
           client="John Cleese", sketch="Cheese Shop Sketch")
