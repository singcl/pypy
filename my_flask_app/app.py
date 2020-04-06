# coding: utf-8

from flask import Flask, escape, url_for, render_template, request,flash, redirect, send_from_directory, make_response, jsonify
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'upload'
ALLOW_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2* 1024 * 1024
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# 目录是否存在,不存在则创建
mkdirlambda =lambda x: os.makedirs(x) if not os.path.exists(x)  else True

@app.route('/')
def index():
    # url_for 构造login url
    login_url = url_for("login")
    response = make_response(f"<a href=\"{login_url}\">登陆</a>")
    response.set_cookie("username", 'singcl')
    return response

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
@app.route('/hello/<name>')
def hello(name=None):
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    return render_template('hello.html', name=name, username=username)

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

# 文件上传
def allowed_files(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOW_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if (request.method == 'POST'):
        # check if the post request has the file part
        if ('file' not in request.files):
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if (file.filename == ''):
            flash('No selected file')
            return redirect(request.url)
        if (not allowed_files(file.filename)):
            flash('不允许上传该类型文件！')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        mkdirlambda(UPLOAD_FOLDER)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload_message.html')

# 浏览上传文件
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    mkdirlambda(UPLOAD_FOLDER)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/json')
def json_res():
    json = make_response(jsonify({"name": "singcl", "home": "https://github.com/singcl"}))
    return json
