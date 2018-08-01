# coding: utf-8

"""
docstring
Python 简单的装饰器
"""


def guess_win(func):
    print '装饰器函数执行...'

    def rooftop_status(*args, **kwargs):
        result = func(*args, **kwargs)
        print "天台已满，请排队！"
        return result

    status = rooftop_status
    return status


# @decorator 的时候装饰器就执行了
# 并不是调用gg_team 时候装饰器才执行
@guess_win
def gg_team(arg):
    print('{}必胜！'.format(arg))
    return '赢了会所嫩模！输了下海干活！'


# x = gg_team('德国')
# y = gg_team('西班牙')

# print x
