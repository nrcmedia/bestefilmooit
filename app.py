# -*- coding: utf-8 -*-
#from __future__ import with_statement
#from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Markup, jsonify
import json
import os


app = Flask(__name__)

app.config['DEBUG'] = True

if os.path.exists('settings_local.py'):
    app.config.from_pyfile('settings_local.py')

# @app.template_filter()
# def htmltotext(html):
#     try:
#         return Markup(html2safehtml(html, ()))
#     except:
#         return ''


@app.route("/")
def index():
    template_args = {}
    return render_template('index.html', **template_args)


app.debug = app.config['DEBUG']

if __name__ == "__main__":
    app.run()
