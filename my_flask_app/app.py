# coding: utf-8

"""Python装饰器在flask中的简单应用
"""
from flask import render_template
from flask.ext.login import login_required, current_user

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/dashboard")
@login_required
def account():
    return render_template("account.html")

