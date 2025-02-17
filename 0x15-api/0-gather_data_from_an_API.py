#!/usr/bin/python3
"""Gather data using api"""
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + user_id

    response = requests.get(url)
    username = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print(f"Employee {username} is done with tasks({done}/{len(tasks)}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")
