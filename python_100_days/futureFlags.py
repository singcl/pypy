#!usr/bin/python
# -*- coding: utf-8 -*-

"""
@see https://segmentfault.com/a/1190000009819359
python并发：使用 futures 处理并发

从网上下载人口前20的国际的国旗
不使用并发：依序下载 下载完一个图片后保存到硬盘，然后请求下一张图片
"""
import os
import time
import sys

import requests  # <1>

POP20_CC = "CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR".split()  # <2>
BASE_URL = 'http://flupy.org/data/flags'  # <3>
DEST_DIR = 'images/'  # <4>


def save_flag(img, filename):  # <5>
    """保存图片"""
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
    path = os.path.join(DEST_DIR, filename)
    try:
        with open(path, "wb") as fp:
            fp.write(img)
    except FileNotFoundError:
        print("无法打开文件", filename)
    except BaseException as e:
        print("无法写入文件", filename)
    else:
        print('保存数据成功！')


def get_flag(cc):  # <6>
    """
    下载图片
    这里我们使用 requests 包，需要先通过pypi安装
    """
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    # js中的请求默认都是异步的。
    # python中的请求默认都是同步的？？
    res = requests.get(url)
    return res.content


def show(text):  # <7>
    """显示一个字符串，然后刷新sys.stdout,目的是在一行消息中看到进度"""
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):  # <8>
    """下载多张图片"""
    for cc in sorted(cc_list):  # <9>
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')
    return len(cc_list)


def main(download_many):  # <10>
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)  # <11>
