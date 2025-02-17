#!/usr/bin/python3
"""exoprt to json file"""
import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users"
    url = user_url + "/" + user_id

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(user_id), 'w') as filename:
        json.dump(dictionary, filename)
