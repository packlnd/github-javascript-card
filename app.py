# -*- coding: utf-8 -*-
from flask import Flask, url_for, make_response, request, current_app
from datetime import timedelta
from functools import update_wrapper
from flask.ext.cors import CORS
from flask.json import jsonify
from util import get_auth, get_token, get_user_data, get_streak, yelp_oauth_client

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def index():
    uname = request.args.get('uname', '')
    streak = get_github_streak(uname)
    return jsonify({'data': streak, 'status': 200})

@app.route('/twitter')
def twitter():
    auth = get_twitter_auth()
    token = get_twitter_token(auth)
    data = get_twitter_user_data(request.args.get('screen_name', ''), token)
    return jsonify(data)

@app.route('/yelp')
def yelp():
    bid = request.args.get('bid','')
    client = get_yelp_client()
    data = client.get_business(bid)
    print data
    return data

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
