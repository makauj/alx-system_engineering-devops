#!/usr/bin/python3
"""
Recursive function
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """
    if after is None:
        after = []

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Python/requests:APIproject:0.0.1'}

    if after:
        url += '?after={}'.format(after)

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    hot_list += [post.get('data').get('title') for post in data.get('children')]

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
