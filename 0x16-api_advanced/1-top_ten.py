#!/usr/bin/python3
"""Querry Reddit API and print the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'My User-Agent 1.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        print(None)
        return
    data = response.json().get('data').get('children')
    for i in range(min(10, len(data))):
        print(data[i].get('data').get('title'))
