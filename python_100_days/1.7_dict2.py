#!usr/bin/python
# -*- coding: utf-8 -*-

"""
字典的常用操作

Version: 0.1
Author: singcl
Date: 2019-01-01

"""


def main():
    stu = {'tom': 23, 'bear': 44, 'hoo': 99}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())

    for elem in stu.items():
        print(elem)
        print(elem[0], elem[1])

    if 'age' in stu:
        stu['age'] = 20
    print(stu)

    stu.setdefault('score', 60)
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)


if __name__ == "__main__":
    main()
