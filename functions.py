import json


def get_todos(filename: str) -> list:
    """Loading list of task from file"""
    with open(filename, 'r') as file_local:
        return json.loads(file_local.read())


def save_todos(filename: str, todos_list_local: list) -> None:
    """Saving current list of task into file"""
    with open(filename, 'w') as file_local:
        json_list = json.dumps(todos_list_local)
        file_local.write(json_list)
