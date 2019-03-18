#!usr/bin/python
# -*- coding: utf-8 -*-

"""
异步I/O操作 - 多线程
Version: 0.1
Author: singcl
Date: 2019-3-18
"""
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print("開始下載%s..." % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%s下載完成！耗時%d秒" % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=("Python 從入門到放棄",))
    t1.start()
    t2 = Thread(target=download, args=("Python 之道",))
    t2.start()

    # join() 作用为阻塞主线程, 即在子线程未返回的时候, 主线程等待其返回然后再继续执行
    # join不能与start在循环里连用
    t1.join()
    t2.join()
    end = time()
    print("總共耗時%.3f秒" % (end - start))


if __name__ == '__main__':
    main()
