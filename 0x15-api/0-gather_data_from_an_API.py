#!/usr/bin/python3
"""Gather data using api"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)

    # Get the name of the employee
    employee = response.json().get("name")
    employee_url = url + "/" + "employee"
    response = requests.get(employee_url)

    # Get the tasks of the employee
    todo_url = url + "/" + "todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    completed_tasks = []

    # Count the number of completed tasks
    for task in tasks:
        if task.get("completed") is True:
            done += 1
            completed_tasks.append(task.get("title"))

    # Print the result
    print("Employee {} is done with tasks({}/{}):"
          .format(employee, done, len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task))