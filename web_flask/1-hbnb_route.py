#!/usr/bin/python3
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
"""
from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)
def display_hello():
    """prints Hello HBNB"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """prints HBNB"""
    return "HBNB"


if __name__ == "__main__":
     app.run(host="0.0.0.0")
