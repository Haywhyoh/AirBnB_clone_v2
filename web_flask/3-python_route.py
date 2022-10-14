#!/usr/bin/python3
'''crates a flask web application'''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    return('HBNB')


@app.route('/c/<text>')
def c_is_fun(text):
    return('C %s' % text.replace("_", " "))


@app.route('/python')
@app.route('/python/<string:text>')
def python_is_fun(text='is cool'):
    """prints Python is cool"""
    text = text.replace("_", " ")
    return "Python %s" % text


if __name__ == "__main__":
    app.run(host='0.0.0.0')
