#!/usr/bin/python
# -*- coding: utf-8 -*-

import aiohttp
import asyncio
import os
from my_lib.retry import retry
from my_lib.time_statistics import time_statistics

"""
协程下载
可以单独执行直接下载
可以用作为模块使用提供一个下载协程

Version: 0.1
Author: Singcl
Date: 2020-01-12
"""


class DownloadTS(object):
    _path: str  # 本地文件路径
    _headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    ts_info: list

    def __init__(self, ts_info: list, path: str = "./resource\\"):
        self.ts_info = ts_info
        self._path = path
        if not os.path.exists(self._path):  # 检测本地目录存在否
            os.makedirs(self._path)

    @retry()
    async def download(self, semaphore=None):
        """
        异步下载 默认最多并发为500
        """
        ts_name, ts_url = self.ts_info
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.get(ts_url) as resp:
                    try:
                        if not resp.status == 200:
                            raise f"网络异常：{resp.status}"

                        with open("{}/{}".format(self._path, ts_name), "wb") as file:
                            content = await resp.read()
                            file.write(content)
                    except Exception as e:
                        print(e)
                    else:
                        print(f"{ts_url} -> OK")

    @time_statistics()
    def run(self):
        semaphore = asyncio.Semaphore(100)
        tasks = []
        tasks.append(asyncio.ensure_future(self.download(semaphore)))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))


if __name__ == "__main__":
    DownloadTS(
        ["xxxx", "http://qlyy369.com/template/helen_ten/js/jquery.lazyload.js"]).run()
