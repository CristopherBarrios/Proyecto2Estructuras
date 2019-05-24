import os
import sys
import requests
from py2neo import Graph, Node, Relationship

def find_tweets(keyword, since_id=-1):
    USER = os.environ["USER"]

    headers = dict(
        Authorization='Bearer'+USER
        )

    payload = dict(
        q= keyword,
        count = 100,
        result_type = "recent",
        lang = "en"
        since_id = since_id
        )

    def upload_tweets(users):
        graph = Graph()

        for t in users:
            u = t['user']
            e = t['password']

            users = graph.merge_one("user","id", t['id'])
            users.properties['text']= t['text']

            user = graph.merge_one("User","username", u["screen_name"])
            
    
