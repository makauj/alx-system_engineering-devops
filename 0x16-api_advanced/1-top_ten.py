#!/usr/bin/python3
"""Querry Reddit API and print the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User-Agent 1.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the status code is not 200, print None and return
        if response.status_code == 404:
            print(None)
            return
        # Extract the data from the JSON response
        data = response.json().get('data').get('children')

        # Print the titles of the first 10 hot posts
        for i in range(min(10, len(data))):
            print(data[i].get('data').get('title'))
    except Exception:
        print(None)
        return
