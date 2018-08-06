# coding=utf-8
"""项目配置文件
Flask应用基本结构配置
"""

DEBUG = False  # Turns on debugging features in Flask
SQLALCHEMY_ECHO = False
BCRYPT_LEVEL = 12  # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "robert@example.com"  # For use in application emails
