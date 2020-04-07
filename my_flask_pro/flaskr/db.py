"""
链接数据库

@Author Singcl<https://github.com/singcl>
@Version 0.0.1
@Data 2020/04/07
"""

import sqlite3

import click
from flask import current_app,g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types = sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
