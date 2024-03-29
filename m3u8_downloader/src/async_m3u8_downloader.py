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
    """
    异步并发下载M3U8资源
    自动合并为媒体文件
    """
    m3u8_name: str # 电影名字
    m3u8_source: str # m3u8路径
    m3u8_directory: str # 电影保存目录
    m3u8_info: list
    m3u8_temp_dir: str # ts文件临时目录

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
        ValueError: too many file descriptors in select()错误和解决
        因为asyncio内部用到了select，而select就是系统打开文件数是有限度的，
        这个其实是操作系统的限制，linux打开文件的最大数默认是1024，windows默认是509，超过了这个值，程序就开始报错
        解决：限制并发量： semaphore = asyncio.Semaphore(100); async with semaphore:
        """
        semaphore = asyncio.Semaphore(100) # 已经要放在这里才生效？？
        ts_urls = self.get_ts_urls()
        tasks = [DownloadTS([f'{index}.ts', url], self.m3u8_temp_dir).download(semaphore)
                 for index, url in enumerate(ts_urls)]
        ft = asyncio.ensure_future(asyncio.wait(tasks))
        ft.add_done_callback(lambda *args: print(f"{self.m3u8_name}完成下载！"))
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

    @time_statistics()
    def run(self):
        """
        下载 => 合并
        """
        self.download()
        self.combine()

def main():
    json_source = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '', '潘甜甜.json')
    with open(json_source, 'r', encoding='utf-8') as f:
        json_source_list = json.load(f)
    # video = json_source_list[-1] # 下载一集
    for video in json_source_list:
        DownloadM3U8([video["name"], video["source"], video["directory"]]).run()

if __name__ == "__main__":
    main()
