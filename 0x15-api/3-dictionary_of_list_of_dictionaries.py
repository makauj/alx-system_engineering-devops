#!/usr/bin/python3
"""List of dictionaries"""
import json
import requests


url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_url = requests.get ('{}/users'.format(url)).json()
    todos_url = requests.get('{}/todos'.format(url)).json()
    user_data = {}
    for user in user_url:
        user_id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == user_id, todos_url))
        user_data = list(map(lambda x: {
            "username": user_name,
            "task": x.get('title'),
            "completed": x.get('completed')
        }, todos))
        user_data['{}'.format(user_id)] = user_data
    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_data, f)
