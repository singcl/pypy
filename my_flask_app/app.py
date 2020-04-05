# coding: utf-8

from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # url_for 构造login url
    login_url = url_for("login")
    return f"<a href=\"{login_url}\">登陆</a>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    profile_url = url_for("show_user_profile", username='singcl')
    base_css_url = url_for("static", filename="style.css")
    return f"""
    <head>
        <link rel="stylesheet" type="text/css" href="{base_css_url}" />
    </head>
    <div style='text-align: center'>
        <p>欢迎来到登陆页面</p>
        <a href="{profile_url}">个人简介</a>
    </div>
    """

@app.route('/hello')
def hello():
    return "hello world"

@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % (escape(username))

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
