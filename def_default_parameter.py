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
