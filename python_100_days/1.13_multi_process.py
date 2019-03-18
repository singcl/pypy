#!usr/bin/python
# -*- coding: utf-8 -*-

"""
多进程
我们启动两个进程，一个输出Ping，一个输出Pong，两个进程输出的Ping和Pong加起来一共10个。听起来很简单吧，但是如果这样写可是错的哦。
Version: 0.1
Author: singcl
Date: 2019-3-18
"""
from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end='', flush=True)
        counter += 1
        sleep(0.01)


def main():
    # 假设你要给一个函数传递一个参数，而这个参数是一个tuple，比如：(12,)，如果你写成(12)，你猜python是会把他当成数字12呢，还是一个tuple？
    # 这样的情况并不少见，比如数学运算，就会用到小括号，python会如何处理呢？加个“, ”，就是明确的告诉python，这是一个tuple。
    Process(target=sub_task, args=('Ping',)).start()
    Process(target=sub_task, args=('Pong',)).start()


if __name__ == '__main__':
    main()
