# coding: utf-8

"""init
"""

# app.py or app/__init__.py
from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# app.config.from_object('config')
# app.config.from_pyfile('config.py')

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')

# Now we can access the configuration variables via app.config["VAR_NAME"].
