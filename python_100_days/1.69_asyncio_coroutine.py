#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Python 并发下载
异步I/O - 非阻塞式I/O操作

Version: 0.1
Author: singcl
Date: 2019-5-17
"""

import asyncio


@asyncio.coroutine
def countdown(name, n):
    while n > 0:
        print(f'Countdown[{name}]: {n}')
        yield from asyncio.sleep(1)
        n -= 1


def main():
    loop = asyncio.get_event_loop()
    tasks = [countdown('A', 10), countdown('B', 5)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == "__main__":
    main()
