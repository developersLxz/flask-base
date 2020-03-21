#!/usr/bin/env python
# encoding: utf-8

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World! Again and again'

    return app
