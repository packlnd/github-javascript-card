import json
import os
import urllib
import base64
import requests
from lxml import html
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from xml.etree import ElementTree

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
fp = os.path.join(SITE_ROOT, 'config.json')

def get_goodreads_data(uid):
    key = get_goodreads_key()
    url = "https://www.goodreads.com/user/show/%s.xml?key=%s" % (uid,key)
    data = requests.get(url)
    return xml_to_json(data)

def xml_to_json(data):
    root = ElementTree.fromstring(data.content)
    user = root[1]
    shelves = user[21]
    data = {
        'name': user[1].text,
        'image': user[4].text,
        'active': user[12].text,
        'shelves': [{
                'name': shelves[0][1].text,
                'count': shelves[0][2].text
            },{
                'name': shelves[1][1].text,
                'count': shelves[1][2].text
            },{
                'name': shelves[2][1].text,
                'count': shelves[2][2].text
            }
        ]
    }
    print data
    return data

def get_github_streak(uname):
    page = requests.get('https://github.com/' + uname)
    tree = html.fromstring(page.content)
    streak = tree.xpath('//span[@class="contrib-number"]/text()')
    return {'data':streak[2].split(" ")[0]}

def get_yelp_data(bid):
    client = get_yelp_client()
    b = client.get_business(bid).business
    return {
        'image_url': b.image_url,
        'name': b.name,
        'city': b.location.city,
        'verified': 'Yes' if b.is_claimed else 'No',
        'rating': b.rating,
        'review_count': b.review_count
    }

def get_yelp_client():
    with open(fp) as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds['yelp'])
        client = Client(auth)
    return client

def get_goodreads_key():
    config = None
    with open(fp) as cred:
        config = json.load(cred)
    return config['goodreads']['key']

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

def get_twitter_user_data(uname):
    auth = get_twitter_auth()
    token = get_twitter_token(auth)
    response = requests.get('https://api.twitter.com/1.1/users/show.json?screen_name=' + uname,
        headers={
            'Authorization': 'Bearer ' + token
        }
    )
    return response.json()
