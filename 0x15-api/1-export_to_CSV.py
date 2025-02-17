#!/usr/bin/python3
"""Export data in the CSV format"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    user = response.json().get('username')
    todo_url = "https://jsonplaceholder.typicode.com/users/todos"
    response = requests.get(todo_url)
    todos = response.json()

    with open(f"{user_id}.csv", 'w') as csvfile:
        for task in todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user_id, user,
                task.get("completed"),
                task.get("title")))
