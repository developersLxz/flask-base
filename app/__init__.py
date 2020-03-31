#!/usr/bin/env python
# encoding: utf-8

import os, sys
from flask import Flask


def create_app():
    app = Flask(__name__,
                instance_path=os.path.join(os.path.abspath(os.curdir),
                                           'instance'),
                instance_relative_config=True)

    # configuration
    if os.path.isdir(app.instance_path) and \
            os.path.isfile(os.path.join(app.instance_path, 'config.py')):
        # append instance folder to import search scope
        sys.path.append(app.instance_path)
        from config import ProductionConfig, DevelopmentConfig, TestingConfig

        if app.config['ENV'] == 'production':
            app.config.from_object(ProductionConfig())
        elif app.config['ENV'] == 'development':
            app.config.from_object(DevelopmentConfig())
        elif app.config['ENV'] == 'testing':
            app.config.from_object(TestingConfig())
        else:
            raise Exception('FLASK_ENV only in (production, development, testing). Your FLASK_ENV is: %s' % (app.config['ENV']))

    else:
        raise Exception(
            'Copy config.py.example to %s AND rename to config.py' %
            (app.instance_path))

    @app.route('/')
    def hello_world():
        return str(DevelopmentConfig().DEBUG)

    return app
