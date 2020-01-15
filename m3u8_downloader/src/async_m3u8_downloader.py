#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
from async_single_downloader import DownloadTS
from my_lib.time_statistics import time_statistics
import os
import json
import m3u8
from urllib.parse import urljoin
from natsort import natsorted
from glob import iglob
import re

"""
协程并发下载

Version: 0.1
Author: Singcl
Date: 2020-01-12
"""


class DownloadM3U8(object):
    m3u8_name: str
    m3u8_source: str
    m3u8_directory: str
    m3u8_info: list
    m3u8_temp_dir: str

    def __init__(self, m3u8_info: list):
        self.m3u8_info = m3u8_info
        self.m3u8_name = m3u8_info[0]
        self.m3u8_source = m3u8_info[1]
        self.m3u8_directory = m3u8_info[2]
        self.m3u8_video_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), self.m3u8_directory)
        self.m3u8_temp_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), self.m3u8_directory, self.m3u8_name)

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
        semaphore = asyncio.Semaphore(100)
        ts_urls = self.get_ts_urls()
        tasks = [DownloadTS([f'{index}.ts', url], self.m3u8_temp_dir).download(semaphore)
                 for index, url in enumerate(ts_urls)]
        ft = asyncio.ensure_future(asyncio.wait(tasks))
        ft.add_done_callback(lambda *args: print("完成下载！"))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(ft)

    def combine(self):
        """
        合并 => 删除
        """
        ts_path = os.path.join(self.m3u8_temp_dir, "*.ts")
        if re.search(r"\.(mp4|avi)$", self.m3u8_name, re.I) == None:
            media_name = f"{self.m3u8_name}.mp4"
        else:
            media_name = self.m3u8_name
        with open(os.path.join(self.m3u8_video_dir, media_name), "wb") as file:
            for ts in natsorted(iglob(ts_path)):
                with open(ts, "rb") as tf:
                    file.write(tf.read())
        #
        for ts in iglob(ts_path):
            os.remove(ts)
        os.rmdir(self.m3u8_temp_dir)

    def run(self):
        self.download()
        self.combine()


@time_statistics
def main():
    json_source = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '', 'download_list.json')
    with open(json_source, 'r', encoding='utf-8') as f:
        json_source_list = json.load(f)
    video = json_source_list[-1]
    DownloadM3U8([video["name"], video["source"], video["directory"]]).run()


if __name__ == "__main__":
    main()
