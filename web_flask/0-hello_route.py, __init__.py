#!usr/bin/python3
"""This is a script to create a basic flask app"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes= False)
def display_hello():
    """Displays 'Hello HBNB!'"""
    return (“Hello HBNB!”)

if __name__ = "__main__":
    app.run(host="0.0.0.0")
