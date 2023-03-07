from db_menager import *


def get_todos(db_file: str) -> list:
    """Loading list of task from database"""
    conn = create_connection(db_file)
    create_todos_table(conn)
    return [val for idx, val in get_whole_table(conn, 'todos')]


def save_todos(db_file: str, todos_list_local: list) -> None:
    """Saving current list of task into file"""
    conn = create_connection(db_file)
    old_todos = [val for idx, val in get_whole_table(conn, 'todos')]
    old_todos_len = len(old_todos)
    new_todos_len = len(todos_list_local)
    if old_todos_len == new_todos_len:
        for i in range(new_todos_len):
            if old_todos[i] != todos_list_local[i]:
                update_task(conn, old_todos[i], todos_list_local[i])
                break
    elif old_todos_len > new_todos_len:
        added_todo = set(old_todos) - set(todos_list_local)
        delete_task(conn, tuple(added_todo))
    elif old_todos_len < new_todos_len:
        added_todo = set(todos_list_local) - set(old_todos)
        insert_task(conn, tuple(added_todo))
