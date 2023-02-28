#!/usr/bin/env python3
"""Set up a basic `Flask` app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return render_template('0-index.html')
