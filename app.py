# -*- coding: utf-8 -*-
from flask import Flask, url_for, make_response, request, current_app
from datetime import timedelta
from functools import update_wrapper
import requests
from lxml import html
from flask.ext.cors import CORS
from flask.json import jsonify
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
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    config = None
    fp = os.path.join(SITE_ROOT, 'config.json')
    with open(fp) as data_file:
        config = json.load(data_file)
    key = urllib.quote_plus(config['key'])
    secret = urllib.quote_plus(config['secret'])
    concat = key + ":" + secret
    bs64 = base64.b64encode(concat)
    return jsonify({'base64':bs64})

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
