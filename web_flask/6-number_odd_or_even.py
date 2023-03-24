#!/usr/bin/python3
""" A script that starts a flask web application """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a Message when /HBNB is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ciscfun(text):
    """ Prints a Message when /c/<text> is called """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """ Prints a Message when /c/<text> is called """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n: int):
    """ Prints a number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n: int):
    """ Prints a number in a template """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n: int):
    """ Prints a number in a template """
    # message = f"{n} is {'even' if n % 2 == 0 else 'odd'}"
    message = '{} is'.format(n)
    message += ' even' if n % 2 == 0 else ' odd'
    return render_template('6-number_odd_or_even.html', message=message)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
