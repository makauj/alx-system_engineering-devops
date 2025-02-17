#!/usr/bin/python3
"""exoprt to json file"""
import json
import requests


def export_to_json():
    """export to json file"""
    url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users'
    user = requests.get(user_url).json()
    user_dict = {}
    for i in user:
        user_dict[i.get('id')] = i.get('username')
    r = requests.get(url)
    data = r.json()
    user_data = {}
    for i in data:
        user_id = i.get('userId')
        if user_id not in user_data:
            user_data[user_id] = []
        user_data[user_id].append({"task": i.get('title'),
                                   "completed": i.get('completed'),
                                   "username": user_dict.get(user_id)})
    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_data, f)
        