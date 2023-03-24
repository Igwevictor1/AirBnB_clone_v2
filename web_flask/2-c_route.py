#!/usr/bin/python3
""" A script that starts a flask web application """
from flask import Flask
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


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
