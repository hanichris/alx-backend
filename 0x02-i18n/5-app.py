#!/usr/bin/env python3
"""Using the `flask-babel` extension."""
from flask import Flask, g, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Return a user dictionary or None if absent."""
    user_id = request.args.get('login_as')
    try:
        user_id = int(user_id)
    except ValueError:
        print("Please use a valid literal for int() with base 10")
    return users.get(user_id)


@app.before_request
def before_request():
    """Find a user, if any, and set it as a global in `flask.g`."""
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def index():
    """Home page of the application.

    First page served to the user of the application.
    """
    return render_template('5-index.html')
