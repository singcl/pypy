# -*- coding: utf-8 -*-
from flask import Flask

"""
构建一个完整的flask应用

@Author Singcl<https://github.com/singcl>
@Version 0.0.1
@Data 2020/04/07
"""

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'
