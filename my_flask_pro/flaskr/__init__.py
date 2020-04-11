"""
__init__.py 有两个作用：一是包含应用工厂；二是告诉 Python flaskr 文件夹应当视作为一个包。

@Author Singcl<https://github.com/singcl>
@Version 0.0.1
@Data 2020/04/07
"""

import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"))

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # 在工厂函数中初始化数据库
    from . import db
    db.init_app(app)

    # 在工厂函数中注册认证蓝图
    from . import auth
    app.register_blueprint(auth.bp)

    # 在工厂函数中注册博客蓝图
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
