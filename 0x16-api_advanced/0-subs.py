#!/usr/bin/python3
"""Reddit API queries to return number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
        return 0
    except Exception:
        return 0
