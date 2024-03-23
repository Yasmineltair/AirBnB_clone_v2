#!/usr/bin/python3
"""  script that starts a Flask web application"""
from flask import Flask


web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def homepage():
    """ homepage"""
    return "Hello HBNB!"


@web_app.route("/hbnb", strict_slashes=False)
def display():
    """ display"""
    return "HBNB"


@web_app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """ c is fun"""
    return 'C {}'.format(text.replace("_", " "))


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
