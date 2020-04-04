# -*- coding: utf-8 -*-
import requests
import re
import time
from lxml import etree

"""
简单的获取Bing每日一图

@Author Singcl<https://github.com/singcl>
@Date 2020/04/04
@Version 0.0.1
"""

host = 'https://cn.bing.com/'

con = requests.get(host)
dom = etree.HTML(con.text)
# 找到bg链接所在的元素，并获取链接相对地址
bg_relative_url = dom.xpath(
    "//div[@id='bgImgProgLoad']/attribute::data-ultra-definition-src")[0]
# 去除开头的‘/’符号
match_obj = re.match(r"^/?(.*)$", bg_relative_url)
# 完整bg URL
url = host + match_obj.group(1)

# 获取图片并保存
bg_name = time.strftime("%Y-%m-%d")
read = requests.get(url)
with open(f"{bg_name}.jpg", 'wb') as f:
    f.write(read.content)
