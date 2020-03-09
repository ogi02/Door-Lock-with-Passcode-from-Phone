# Standard Library Imports
from os import urandom

# Third Party Imports
from flask import Flask
from functools import wraps

# app config
app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(32)