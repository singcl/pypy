#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
from async_single_downloader import DownloadTS
from my_lib.time_statistics import time_statistics
import os
import json

"""
协程并发下载

Version: 0.1
Author: Singcl
Date: 2020-01-12
"""


@time_statistics
def main():
    json_source = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '', 'download_list.json')
    with open(json_source, 'r', encoding='utf-8') as f:
        json_source_list = json.load(f)

    tasks = [asyncio.ensure_future(DownloadTS(
        [item["name"], item["source"]]).download()) for item in json_source_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == "__main__":
    main()
