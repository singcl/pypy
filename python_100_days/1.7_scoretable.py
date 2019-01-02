#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python 学生考试成绩表

Version: 0.1
Author: singcl
Date: 2019-01-02

"""


def main():
    names = ['zhangsan', 'lisi', 'wanger', 'lijing', 'hekai']
    subjs = ['语文', '数学', '英语']

    scores = [[0] * 3] * 5
    for row, name in enumerate(names):
        print("请输入%s的成绩" % name)
        for col, subj in enumerate(subjs):
            scores[row][col] = float(input(subj + ':'))

    print(scores)


if __name__ == '__main__':
    main()
