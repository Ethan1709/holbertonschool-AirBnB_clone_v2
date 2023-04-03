#!/usr/bin/python3
"""hello flask"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello HBNB</p>"