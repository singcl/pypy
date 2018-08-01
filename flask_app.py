# coding=utf-8
"""简单的flask应用"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    app.run()
