# data structure to store tasks
todos_list = []

# main loop
while True:
    # user choice
    user_action = input("Type add, show, edit, complete or exit:").strip()
    user_action = user_action.strip()

    # add task
    if user_action.startswith("add") or user_action.startswith("new"):
        if user_action == 'add' or user_action == 'new':
            user_todo = input("Enter a todo:")
        elif user_action[3] == ' ':
            user_todo = user_action.split(' ', 1)[1]
        todos_list.append(user_todo)
    # display tasks
    elif user_action == 'show' or user_action == 'display':
        print("---------- TODO LIST ----------")
        for idx, todo in enumerate(todos_list):
            print(f"{idx+1}-{todo}" )
        print("-------------------------------")
    # edit task
    elif user_action == 'edit':
        user_choice = input("Chose item you want to edit:")
        try:
            user_choice = int(user_choice) - 1
            edited_todo = input("On what you want to change todo:", todos_list[user_choice])
            todos_list[user_choice] = edited_todo
        except IndexError:
            print("you select task that is not on the list")
        except ValueError:
            print("please use number of task that you want to edit")
    # complete task
    elif user_action.startswith('complete '):
        if user_action == "complete":
            user_choice = input("Chose item you want to complete:")
        elif user_action[8] == ' ':
            user_choice = user_action.split(' ', 1)[1]
        try:
            user_choice = int(user_choice) - 1
            todos_list.pop(user_choice)
        except IndexError:
            print("you select task that is not on the list")
        except ValueError:
            print("please use number of task that you want to complete")
    # exit app
    elif user_action == 'exit':
        break
    # wrong user command
    else:
        print("not any cases match!")



