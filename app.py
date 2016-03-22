# -*- coding: utf-8 -*-
from flask import Flask, url_for, make_response, request, current_app
from datetime import timedelta
from functools import update_wrapper
import requests
from lxml import html
from flask.ext.cors import CORS
from flask.json import jsonify
from util import get_auth, get_token, get_user_data
import json
import os
import urllib
import base64

app = Flask(__name__, static_url_path='')
CORS(app)

def get_streak(uname):
    page = requests.get('https://github.com/' + uname)
    tree = html.fromstring(page.content)
    streak = tree.xpath('//span[@class="contrib-number"]/text()')
    return streak[2].split(" ")[0]

@app.route('/')
def index():
    uname = request.args.get('uname', '')
    streak = get_streak(uname)
    return jsonify({'data': streak, 'status': 200})

@app.route('/twitter')
def twitter():
    auth = get_auth()
    token = get_token(auth)
    data = get_user_data('vincentmvdm', token)
    return jsonify(data)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
