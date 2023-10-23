#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import requests
import sys
import json

def get_employee_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    user_id = user_data.get("id")
    user_name = user_data.get("name")

    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    user_data_json = {user_id: []}

    for todo in todos_data:
        task_data = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user_name
        }
        user_data_json[user_id].append(task_data)

    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(user_data_json, json_file, indent=4)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_list_progress(employee_id)
