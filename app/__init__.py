#!/usr/bin/env python
# encoding: utf-8

import os
from flask import Flask

def create_app():
    app = Flask(__name__,
            instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'),
            instance_relative_config=True)

    @app.route('/')
    def hello_world():
        return app.instance_path

    return app
