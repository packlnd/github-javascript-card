# -*- coding: utf-8 -*-
from flask import Flask, url_for, make_response, request, current_app
from datetime import timedelta
from functools import update_wrapper
from flask.ext.cors import CORS
from flask.json import jsonify
from util import get_twitter_auth, get_twitter_token, get_twitter_user_data, get_github_streak, get_yelp_client
import yaml
import json

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
    b = client.get_business(bid).business
          #data['image_url'],
          #data['name'],
          #data['rating'],
          #'#c41200',
          #false,'','',data['review_count'],"Reviews",
          #false,'','',data['review_count'],"Reviews",
          #false,'','',data['review_count'],"Reviews",
    return jsonify({
        'image_url': b.image_url,
        'name': b.name,
        'city': b.location.city,
        'category': b.categories[0][0],
        'rating': b.rating,
        'review_count': b.review_count
    })

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
