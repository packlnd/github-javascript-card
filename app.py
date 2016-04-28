# -*- coding: utf-8 -*-
from flask import Flask, url_for, make_response, request, current_app
from datetime import timedelta
from functools import update_wrapper
from flask.ext.cors import CORS
from flask.json import jsonify
from util import get_twitter_user_data, get_github_streak, get_yelp_data, get_goodreads_data
import yaml
import json

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def index():
    uname = request.args.get('uname', '')
    streak = get_github_streak(uname)
    return jsonify(streak)

@app.route('/twitter')
def twitter():
    sname = request.args.get('screen_name', '')
    data = get_twitter_user_data(sname)
    return jsonify(data)

@app.route('/yelp')
def yelp():
    bid = request.args.get('bid','')
    data = get_yelp_data(bid)
    return jsonify(data)

@app.route('/goodreads')
def goodreads():
    uid = request.args.get('uid','')
    data = get_goodreads_data(uid)
    return jsonify(data)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
