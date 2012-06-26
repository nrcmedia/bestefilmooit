# -*- coding: utf-8 -*-
#from __future__ import with_statement
#from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Markup, jsonify
import json
import os
from imdb import IMDb

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


@app.route("/search")
def search():
    title = request.args.get('q', '')
    ia = IMDb()
    movies = ia.search_movie(title)
    results = []
    for movie in movies:
        # print dir(result)
        # print movie['long imdb title']
        results.append({'value': movie.movieID, 'name': movie['long imdb title']})
    # print results
    return json.dumps(results)


@app.route("/save")
def save():
    favs = request.args.get('favs', '')
    return render_template('save.html', {'favs': favs})


app.debug = app.config['DEBUG']

if __name__ == "__main__":
    app.run()
