#!usr/bin/python
# -*- coding: utf-8 -*-

"""
多线程
我们可以直接使用threading模块的Thread类来创建线程，
也可以通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程
Version: 0.1
Author: singcl
Date: 2019-3-18
"""
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTread(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("開始下載%s..." % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print("%s下載完成！耗時%d秒" % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTread("Python 從入門到放棄")
    t1.start()
    t2 = DownloadTread("Python 之道")
    t2.start()

    # join() 作用为阻塞主线程, 即在子线程未返回的时候, 主线程等待其返回然后再继续执行
    # join不能与start在循环里连用
    t1.join()
    t2.join()
    end = time()
    print("總共耗時%.3f秒" % (end - start))


if __name__ == '__main__':
    main()
