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
            app.config.from_object(ProductionConfig(app))
        elif app.config['ENV'] == 'development':
            app.config.from_object(DevelopmentConfig(app))
        elif app.config['ENV'] == 'testing':
            app.config.from_object(TestingConfig(app))
        else:
            raise Exception(
                'FLASK_ENV only in (production, development, testing). Your FLASK_ENV is: %s'
                % (app.config['ENV']))

    else:
        raise Exception(
            'Copy config.py.example to %s AND rename to config.py' %
            (app.instance_path))

    # logging
    import logging
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    from logging.handlers import TimedRotatingFileHandler
    handler = TimedRotatingFileHandler(**app.config['LOG_PARAMETERS'])
    handler.setLevel(app.logger.level)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    @app.route('/')
    def index():
        app.logger.info("Index Page")
        return "Index"

    @app.route('/hello/<name>', defaults={'gender': None})
    @app.route('/hello/<name>/<gender>')
    def hello(name, gender):
        ret = 'Hello! '

        if gender == 'male':
            ret += 'Mr '
        elif gender == 'female':
            ret += 'Miss '
        else:
            pass

        return ret + name

    @app.route('/calculate/<string:expression>')
    def calculate(expression):
        app.logger.debug(type(expression))
        return str(eval(expression))

    return app
