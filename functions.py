from tkinter import END

def get_todos(filename: str) -> list:
    """Loading list of task from file"""
    with open(filename, 'r') as file_local:
        todos_list_local = file_local.readlines()
        return [todo_local.strip('\n') for todo_local in todos_list_local]

def save_todos(filename: str, todos_list_local: list) -> None:
    """Saving current list of task into file"""
    with open(filename, 'w') as file_local:
        for todo_local in todos_list_local:
            file_local.write(todo_local + "\n")

def add_todos(entry, listbox, todo_list, filename="todo.txt") -> None:
    """Add new task to listbox and file"""
    new_val = entry.get()
    todo_list = list(todo_list.get())
    todo_list.append(new_val)
    entry.delete(0, END)
    save_todos(filename, todo_list)
    listbox.insert(END, new_val)

def edit_todos(entry, listbox, todo_list, filename="todo.txt") -> None:
    """Edit existing item in listbox and file"""
    new_val = entry.get()
    index_of_item = listbox.curselection()[0]
    todo_list = list(todo_list.get())
    todo_list[index_of_item] = new_val
    entry.delete(0, END)
    save_todos(filename, todo_list)
    listbox.delete(index_of_item)
    listbox.insert(index_of_item, new_val)
def delete_todos(entry, listbox, todo_list, filename="todo.txt"):
    new_val = entry.get()
    index_of_item = listbox.curselection()[0]
    todo_list = list(todo_list.get())
    todo_list.remove(new_val)
    entry.delete(0, END)
    save_todos(filename, todo_list)
    listbox.delete(index_of_item)