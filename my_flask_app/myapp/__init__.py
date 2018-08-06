# coding: utf-8

"""init
"""

# app.py or app/__init__.py
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Now we can access the configuration variables via app.config["VAR_NAME"].
