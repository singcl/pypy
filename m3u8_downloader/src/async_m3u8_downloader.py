#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
from async_single_downloader import DownloadTS
from my_lib.time_statistics import time_statistics
import os
import json
import m3u8
from urllib.parse import urljoin

"""
协程并发下载

Version: 0.1
Author: Singcl
Date: 2020-01-12
"""


class DownloadM3U8(object):
    m3u8_name: str
    m3u8_source: str
    m3u8_info: list

    def __init__(self, m3u8_info: list):
        self.m3u8_info = m3u8_info
        self.m3u8_name = m3u8_info[0]
        self.m3u8_source = m3u8_info[1]

    def get_ts_urls(self):
        """
        解析标准的m3u8文件
        """
        m3u8_obj = m3u8.load(self.m3u8_source)
        base_uri = m3u8_obj.base_uri
        for seg in m3u8_obj.segments:
            yield urljoin(base_uri, seg.uri)

    def download(self):
        """
        并发下载m3u8所有TS文件
        """
        ts_urls = self.get_ts_urls()
        tasks = [asyncio.ensure_future(DownloadTS([f'{index}.ts', url]).download())
                 for index, url in enumerate(ts_urls)]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))


@time_statistics
def main():
    json_source = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '', 'download_list.json')
    with open(json_source, 'r', encoding='utf-8') as f:
        json_source_list = json.load(f)
    video = json_source_list[-1]
    DownloadM3U8([video["name"], video["source"]]).download()


if __name__ == "__main__":
    main()
