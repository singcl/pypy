#!/usr/bin/python
# -*- coding: utf-8 -*-

from async_m3u8_downloader import DownloadM3U8
import json
import sys
import os

"""
M3U8电影下载
python main.py 这样会使用目录中默认json: download_list.json
python main.py your_json_file 这样会下载指定的json文件

Version: 0.1
Author: Singcl
Date: 2020-01-15
"""


def main(json_path: str = 'download_list.json', number=None):
    json_source = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), json_path)
    with open(json_source, 'r', encoding='utf-8') as f:
        json_source_list = json.load(f)

    if number is not None:
        video = json_source_list[int(number) - 1]  # 下载一集
        DownloadM3U8([video["name"], video["source"],
                      video["directory"]]).run()
    else:
        for video in json_source_list:
            DownloadM3U8([video["name"], video["source"],
                          video["directory"]]).run()


if __name__ == "__main__":
    """
    通过sys模块来识别参数
    """
    try:
        json_file = sys.argv[1]
        number = sys.argv[2]
    except IndexError as e:
        main()
    else:
        main(json_file, number)
