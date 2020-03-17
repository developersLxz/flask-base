#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello_world():
    return 'Hello, World! Again and again'
