# coding: utf-8

"""派生类可能会覆盖其基类的方法。
因为方法调用同一个对象中的其它方法时没有特权，基类的方法调用同一个基类的方法时，
可能实际上最终调用了派生类中的覆盖方法(对于 C++ 程序员来说，Python 中的所有方法本质上都是 虚 方法)。
"""


# 基类
class Base:
    def __init__(self):
        self.count = 0

    def xx(self):
        self.count += 1
        print 'singcl - base'

    def yy(self):
        self.xx()


# 派生类
class Sub(Base):
    def __init__(self):
        self.count = 0

    def xx(self):
        self.count += 1
        print 'singcl - Sub'


r = Base()
r.yy()

# 在子类调用yy方法时候 self指的是子类
sr = Sub()
sr.yy()
