#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Python 并发下载
异步I/O - 非阻塞式I/O操作

Version: 0.1
Author: singcl
Date: 20120-01-14
@aiohttp 0.17.4
"""

import asyncio
import aiohttp


def get_body(url):
    response = yield from aiohttp.request("GET", url)
    return (yield from response.read())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    raw_html = loop.run_until_complete(get_body("http://python.org"))
    print(raw_html)
