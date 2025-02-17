#!/usr/bin/python3
"""Gather data using api"""
import requests
import sys
import json


def get_data(employee_id):
    """Get data from api"""
    url = "https://jsonplaceholder.typicode.com"
    user_res = requests.get(url + "/users/{}".format(employee_id))
    user = user_res.json()
    if not user:
        return (None, None)
    todos_res = requests.get(url + "/todos", params={"userId": employee_id})
    todos = todos_res.json()
    if not todos:
        return (None, None)

    return (user, todos)


def export_data(employee_id):
    """Export data to json"""
    user, todos = get_data(employee_id)
    if not user or not todos:
        return
    username = user.get("username")
    data = []
    for todo in todos:
        data.append({"task": todo.get("title"),
                     "completed": todo.get("completed"),
                     "username": username})
    with open("{}.json".format(employee_id), "w") as jsonfile:
        jsonfile.write(json.dumps({employee_id: data}))
