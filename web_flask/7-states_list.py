#!/usr/bin/python3
"""  script that starts a Flask web application: """
from flask import Flask, render_template
from models import storage


web_app = Flask(__name__)


@web_app.route("/states_list", strict_slashes=False)
def states_list():
    """ list of states"""
    states = sorted(list(storage.all("State").values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@web_app.teardown_appcontext
def tear_down(error):
    """ tear down method"""
    storage.close()


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
