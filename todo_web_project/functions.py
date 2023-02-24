FILE_NAME = r'todo_web_project\todo.txt'


def get_todos(filename=FILE_NAME) -> list:
    """Loading list of task from file"""
    with open(filename, 'r') as file_local:
        todos_list_local = file_local.readlines()
        return [todo_local.strip('\n') for todo_local in todos_list_local]


def save_todos(todos_list_local: list, filename=FILE_NAME) -> None:
    """Saving current list of task into file"""
    with open(filename, 'w') as file_local:
        for todo_local in todos_list_local:
            file_local.write(todo_local + "\n")