from functions import *

source_file = 'todo.txt'
# loading data from file
try:
    todo_list = get_todos(source_file)
except FileNotFoundError as error:
    print(error, "file with save todos is not present!")
    todos_list = []

# main loop
while True:
    # user choice
    user_action = input("Type add, show, edit, complete or exit:").strip()
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        if user_action == 'add' or user_action == 'new':
            user_todo = input("Enter a todo:")
        elif user_action[3] == ' ':
            user_todo = user_action.split(' ', 1)[1]
        todos_list.append(user_todo)
        save_todos(source_file, todos_list)
    elif user_action == 'show' or user_action == 'display':
        print("---------- TODO LIST ----------")
        for idx, todo in enumerate(todos_list):
            print(f"{idx+1}-{todo}" )
        print("-------------------------------")
    elif user_action == 'edit':
        user_choice = input("Chose item you want to edit:")
        try:
            user_choice = int(user_choice) - 1
            edited_todo = input("On what you want to change todo:", todos_list[user_choice])
            todos_list[user_choice] = edited_todo
            save_todos(source_file, todos_list)
        except IndexError:
            print("you select task that is not on the list")
        except ValueError:
            print("please use number of task that you want to edit")
    elif user_action.startswith('complete '):
        if user_action == "complete":
            user_choice = input("Chose item you want to complete:")
        elif user_action[8] == ' ':
            user_choice = user_action.split(' ', 1)[1]
        try:
            user_choice = int(user_choice) - 1
            todos_list.pop(user_choice)
            save_todos(source_file, todos_list)
        except IndexError:
            print("you select task that is not on the list")
        except ValueError:
            print("please use number of task that you want to complete")
    elif user_action == 'exit':
        break
    else:
        print("not any cases match!")



