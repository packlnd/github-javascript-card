import json
import os
import urllib
import base64
import requests
from lxml import html

def get_streak(uname):
    page = requests.get('https://github.com/' + uname)
    tree = html.fromstring(page.content)
    streak = tree.xpath('//span[@class="contrib-number"]/text()')
    return streak[2].split(" ")[0]

def get_auth():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    config = None
    fp = os.path.join(SITE_ROOT, 'config.json')
    with open(fp) as data_file:
        config = json.load(data_file)
    return config['base64']

def get_token(auth):
    response = requests.post(
        'https://api.twitter.com/oauth2/token',
        data='grant_type=client_credentials',
        headers={
            'Authorization': 'Basic ' + auth,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
    )
    return response.json()['access_token']


def get_user_data(uname, token):
    response = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name' + uname,
        headers={
            'Authorization': 'Bearer ' + token
        }
    )
    return response.json()
