"""This is a script to create a basic flask app"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes= False)
def display_hello():
    return (“Hello HBNB!”)

if __name__ = "__main__":
    app.run(debug=True)
