import os
import sys
import requests
from py2neo import Graph, Node, Relationship

def find_tweets(keyword, since_id=-1):
    TWITTER_BEARER = os.environ["TWITTER_BEARER"]

    headers = dict(
        accept='application/json',
        Authorization='Bearer'+TWITTER_BEARER
        )

    payload = dict(
        q= keyword,
        count = 100,
        result_type = "recent",
        lang = "en"
        since_id = since_id
        )
    
