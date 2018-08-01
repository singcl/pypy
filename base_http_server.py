#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""使用原生的python开发的web服务器，入门级！"""

import os   # Python的标准库中的os模块包含普遍的操作系统功能
import re   # 引入正则表达式对象
import urllib   # 用于对URL进行编解码
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler  # 导入HTTP处理相关的模块


class TestHTTPHandler(BaseHTTPRequestHandler):
    """自定义处理程序，用于处理HTTP请求"""

    def do_GET(self):
        """处理GET请求"""
        # 获取URL
        print 'URL=',self.path
        # 页面输出模板字符串
        template_str = '''
            <html>   
            <head>   
                <title>QR Link Generator</title>   
            </head>   
            <body>   
                <h3>Hello Singcl! Powered by Python</h3>
            </body>   
            </html>
        '''

        self.protocal_version = 'HTTP/1.1'  # 设置协议版本
        self.send_response(200) # 设置响应状态码
        self.send_header("Welcome", "Contect")  # 设置响应头
        self.end_headers()
        self.wfile.write(template_str)   # 输出响应内容


# 启动服务函数
def start_server(port):
        http_server = HTTPServer(('', int(port)), TestHTTPHandler)
        http_server.serve_forever() # 设置一直监听并接收请求


# os.chdir('static')  #改变工作目录到 static 目录
start_server(8005)  # 启动服务，监听8005端口