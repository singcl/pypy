# -*- coding: utf-8 -*-
import os
import time
import m3u8
import requests
from glob import iglob
from natsort import natsorted
from urllib.parse import urljoin
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor

"""
a dataclass that describes a programming language
dataclass: https://www.jianshu.com/p/bea5c202cf85

Version: 0.1
Author: Singcl
Date: 2019-12-29
Github: https://github.com/singcl/pypy
"""

TS_DIR = "video"


@dataclass
class DownLoad_M3U8(object):
    """
    Python 3.7 将于今年夏天发布，Python 3.7 中将会有许多新东西
    最激动人心的新功能之一是 dataclass 装饰器。
    py3.8 类型标注支持
    """
    m3u8_url: str
    file_name: str

    def __post_init__(self):
        """dataclass 附加处理"""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', }
        self.threadpool = ThreadPoolExecutor(max_workers=10)
        if not self.file_name:
            self.file_name = 'new.mp4'

    def get_ts_url(self):
        """
        解析标准的m3u8文件
        """
        m3u8_obj = m3u8.load(self.m3u8_url)
        base_uri = m3u8_obj.base_uri

        for seg in m3u8_obj.segments:
            yield urljoin(base_uri, seg.uri)

    def download_single_ts(self, urlinfo):
        """
        同步下载单个TS文件并写入本地
        """
        url, ts_name = urlinfo
        res = requests.get(url, headers=self.headers)
        with open("{}/{}".format(TS_DIR, ts_name), 'wb') as fp:
            fp.write(res.content)

    def download_all_ts(self):
        """
        线程池下载所有ts文件
        """
        ts_urls = self.get_ts_url()
        for index, ts_url in enumerate(ts_urls):
            print(ts_url)
            self.threadpool.submit(self.download_single_ts, [
                                   ts_url, f'{index}.ts'])
        self.threadpool.shutdown()

    def run(self):
        """
        下载 => 合并 => 删除
        """
        self.download_all_ts()
        ts_path = f'{TS_DIR}/*.ts'
        with open(f'{TS_DIR}/{self.file_name}', 'wb') as fn:
            for ts in natsorted(iglob(ts_path)):
                with open(ts, 'rb') as ft:
                    ts_slice = ft.read()
                    fn.write(ts_slice)
        for ts in iglob(ts_path):
            os.remove(ts)


if __name__ == '__main__':

    m3u8_url = 'https://v3.szjal.cn/20191220/eOuDB137/800kb/hls/index.m3u8'
    file_name = ''

    start = time.time()

    M3U8 = DownLoad_M3U8(m3u8_url, file_name)
    M3U8.run()

    end = time.time()
    print('耗时:', "{}ms".format(end - start))
