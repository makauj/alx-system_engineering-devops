#!/usr/binpython3
"""List of dictionaries"""
import json
import requests


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(user_url)
    users = response.json()
    users_dict = {}
    for user in users:
        user_id = user.get("id")
        users_dict[user_id] = []
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todo_url)
    todos = response.json()
    for todo in todos:
        task = {}
        user_id = todo.get("userId")
        task["username"] = users_dict[user_id]
        task["task"] = todo.get("title")
        task["completed"] = todo.get("completed")
        users_dict[user_id].append(task)
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(users_dict, jsonfile)
