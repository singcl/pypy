#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 轮播welcome

Version: 0.1
Author: singcl
Date: 2019-01-02

"""
import os
import time


def main():
    str1 = 'Welcome'
    while True:
        print(str1)
        time.sleep(0.2)
        str1 = str1[1:] + str1[0:1]
        # for Windows use os.system('cls') instead
        os.system('clear')


if __name__ == '__main__':
    main()
