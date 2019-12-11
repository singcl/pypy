#!usr/bin/python
# -*- coding: utf-8 -*-
"""
Python 并发下载
异步I/O - 非阻塞式I/O操作

Version: 0.1
Author: singcl
Date: 2019-5-18
"""

import asyncio
import aiohttp


async def download(url):
    print('Fetch:', url)
    # 异步上下文管理器”async with”
    # @see https://blog.csdn.net/tinyzhao/article/details/52684473
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(url, '--->', resp.status)
            print(url, '--->', resp.cookies)
            print('\n\n', await resp.text())


def main():
    loop = asyncio.get_event_loop()
    urls = [
        # 'https://www.baidu.com',
        # 'http://www.sohu.com/',
        # 'http://www.sina.com.cn/',
        # 'https://www.jd.com/',
        'https://www.taobao.com/',
        'https://imcoco.top'
    ]
    corutines = [download(url) for url in urls]
    loop.run_until_complete(asyncio.wait(corutines))
    loop.close()


if __name__ == '__main__':
    main()
