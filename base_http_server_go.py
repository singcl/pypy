# coding: utf-8

"""
简单的HTTP Server用于测试GO 的json反编译
"""

import BaseHTTPServer
import json


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
    处理请求返回
    """

    vc = {
        "Status": {
            "Text": "This is the Go Json Text: Use Python SimpleHTTPServer build"
        }
    }

    # 处理GET请求
    def do_GET(self):
        self.send_response(200, 'success')
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(json.dumps(self.vc))))
        self.end_headers()
        self.wfile.write(json.dumps(self.vc))


"""----------------------------------------------------------------------"""

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
