
user_prompt = "Enter a todo:"

try:
    with open('todos.txt', 'r') as file:
        todos_list = file.readlines()
except:
    print("file with save todos is not present!")
    todos_list = []

while True:
    user_action = input("Type add, show, edit, complete or exit:").strip()
    user_action = user_action.strip()

    match user_action:
        case 'add':
            user_todo = input(user_prompt)
            todos_list.append(user_todo + "\n")
            with open('todos.txt', 'a') as file:
                file.write(user_todo + "\n")
        case 'show' | 'display':
            for idx, todo in enumerate(todos_list):
                print(f"{idx+1}-{todo}", end='')
        case 'edit':
            user_choice = input("Chose item you want to edit:")
            user_choice = int(user_choice) - 1
            edited_todo = input("On what you want to change todo:", todos_list[user_choice])
            todos_list[user_choice] = edited_todo
        case 'complete':
            user_choice = input("Chose item you want to complete:")
            user_choice = int(user_choice) -1
            todos_list.pop(user_choice)
        case 'exit':
            break
        case _ :
            print("not any cases match!")


