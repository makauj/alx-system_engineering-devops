#!/usr/bin/python3
"""
Recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces
"""
import requests
from collections import defaultdict


def count_words(subreddit, word_list, after=None, word_dict={}):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    if word_dict is None:
        word_dict = defaultdict(int)

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params={'limit': 100, 'after': after})

    if response.status_code != 200:
        return

    data = response.json().get('data')
    after = data.get('after')

    for child in data.get('children'):
        title = child.get('data').get('title').lower().split()
        for word in word_list:
            if word.lower() in title:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    if after is None:
        if len(word_dict) == 0:
            return

        for key, value in sorted(word_dict.items(),
                                 key=lambda x: (-x[1], x[0])):
            print('{}: {}'.format(key, value))
    else:
        return count_words(subreddit, word_list, after, word_dict)
