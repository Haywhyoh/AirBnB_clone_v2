#!/usr/bin/python3
'''crates a flask web application'''
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return ('Hello HBNB')


@app.route('/hbnb')
def hbnb():
    return ('HBNB')


@app.route('/c/<string:text>')
def c_is_fun(text):
    return "C %s" % text.replace('_', ' ')


@app.route('/python')
@app.route('/python/<string:text>')
def python_is_fun(text='is cool'):
    """prints Python is cool"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>')
def num(n):
    return ("%d is a number" % n)

@app.route('/number_template/<int:n>')
def check_num(n):
    return render_template('5-numnber.html', n=n)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
