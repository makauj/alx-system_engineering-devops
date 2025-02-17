#!/usr/bin/python3
"""exoprt to json file"""
import json
import requests
import sys


def export_to_json():
    """export to json file"""
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_url = url + "/users/" + user_id
    todos_url = url + "/todos"
    user = requests.get(user_url)
    todos = requests.get(todos_url)

    username = user.json().get('username')
    tasks = todos.json()

    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open(user_id + ".json", 'w') as f:
        json.dump(dictionary, f)
