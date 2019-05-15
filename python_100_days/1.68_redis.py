#!usr/bin/python
# -*- coding: utf-8 -*-
"""
在Python程序中使用Redis
@see http://redisdoc.com/
Version: 0.1
Author: singcl
Date: 2019-5-16
"""
import redis


def main():
    client = redis.Redis(host="127.0.0.1", port="6379", password="football")
    client.set('username2', 'admin')
    client.hset('student', 'age', 38)
    client.keys('*')


if __name__ == "__main__":
    main()
