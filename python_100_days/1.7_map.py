#!usr/bin/python
# -*- coding: utf-8 -*-

"""
Python dict字典数据结构
字典是另一种可变容器模型，类似于我们生活中使用的字典，它可以存储任意类型对象，
与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开

Version: 0.1
Author: singcl
Date: 2018-12-25

"""


def main():
    scores = {"tom": 74, "jack": 33, "sin": 43}
    # 通过键可以获取字典中对应的值
    print(scores['tom'])

    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for key in scores:
        print("%s\t ----> \t%s" % (key, scores[key]))

    # 更新字典中的元素
    scores["tom"] = 32
    scores["jack"] = 99
    scores["sin"] = 37

    print(scores)

    if ('jim' in scores):
        print(scores['jim'])

    print(scores.get('jim'))
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('jim', 12))

    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('jim', 100))

    # 清空字典
    scores.clear()
    print(scores)


if __name__ == "__main__":
    main()
