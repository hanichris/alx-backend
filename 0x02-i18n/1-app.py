#!/usr/bin/env python3
"""Using the `flask-babel` extension."""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Base config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """Home page of the application.

    First page served to the user of the application.
    """
    return render_template('1-index.html')
