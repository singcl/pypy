# coding: utf-8

"""
docstring
Python 简单的装饰器
"""


def guess_win(func):
    def rooftop_status(*args, **kwargs):
        result = func(*args, **kwargs)
        print "天台已满，请排队！"
        return result

    status = rooftop_status
    return status


@guess_win
def gg_team(arg):
    print('{}必胜！'.format(arg))
    return '赢了会所嫩模！输了下海干活！'


x = gg_team('德国')
# y = gg_team('西班牙')

print x
