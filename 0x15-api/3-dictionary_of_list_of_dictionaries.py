#!/usr/bin/python3
"""Gather data using api"""
import json
import requests


url = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    users = requests.get('{}/users'.format(url)).json()
    todo_requests = requests.get('{}/todos'.format(url)).json()
    users_data = {}
    for user in users:
        id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todo_requests))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_data['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
