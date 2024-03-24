#!/usr/bin/python3
""" a script that starts a Flask web application:"""
from flask import Flask


web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def homepage():
    """ home page"""
    return "Hello HBNB!"


@web_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb"""
    return "HBNB"


@web_app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    """ display “C ”, followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@web_app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@web_app.route("/python/<text>", strict_slashes=False)
def py(text):
    """ display “Python ”, followed by the value of the text"""
    return "Python {}".format(text.replace("_", " "))


@web_app.route("/number/<int:n>")
def number(n):
    """ display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@web_app.route("/number_template/<int:n>", strict_slashes=False)
def temp(n):
    """ display a HTML page only if n is an integer"""
    return render_template("5-number.html")


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
