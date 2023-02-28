#!/usr/bin/env python3
"""Using the `flask-babel` extension."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Base config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Select a language translation to use for a request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Home page of the application.

    First page served to the user of the application.
    """
    return render_template('3-index.html')
