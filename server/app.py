# -*- coding: utf-8 -*-
from flask import Flask, request
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
import requests
from lxml import html
from flask.ext.cors import CORS
from flask.json import jsonify
import json

app = Flask(__name__)
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
    config = None
    with open('data.json') as data_file:
        config = json.load(data_file)
    return config

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
