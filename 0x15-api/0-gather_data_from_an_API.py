#!/usr/bin/python3
"""Gather data using api"""
import requests
import sys


def get_data(employee_id):
    """Get data from api"""
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(employee_id)).json()

    todos = requests.get(url + "/todos", params={"userId": employee_id}).json()
    return user, todos


def export_data(employee_id):
    """Export data to csv"""
    user, todos = get_data(employee_id)
    employee_name = user.get("username")
    filename = "{}.csv".format(employee_id)

    with open(filename, "w") as f:
        for todo in todos:
            f.write('"{}","{}","{}","{}"\n'.format(
                employee_id, employee_name,
                todo.get("completed"), todo.get("title")))
    return filename
