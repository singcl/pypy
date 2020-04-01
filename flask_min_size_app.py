"""
一个最小的应用
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

# $ export FLASK_APP=flask_min_size_app.py
# $ flask run
# * Running on http://127.0.0.1:5000/
