import json
import os
import urllib
import base64
import requests
from lxml import html
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
fp = os.path.join(SITE_ROOT, 'config.json')

def get_github_streak(uname):
    page = requests.get('https://github.com/' + uname)
    tree = html.fromstring(page.content)
    streak = tree.xpath('//span[@class="contrib-number"]/text()')
    return streak[2].split(" ")[0]

def get_yelp_client():
    with open(fp) as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds['yelp'])
        client = Client(auth)
    return client

def get_twitter_auth():
    config = None
    with open(fp) as cred:
        config = json.load(cred)
    return config['twitter']['base64']

def get_twitter_token(auth):
    response = requests.post(
        'https://api.twitter.com/oauth2/token',
        data='grant_type=client_credentials',
        headers={
            'Authorization': 'Basic ' + auth,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
    )
    return response.json()['access_token']

def get_twitter_user_data(uname, token):
    response = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + uname,
        headers={
            'Authorization': 'Bearer ' + token
        }
    )
    return response.json()
