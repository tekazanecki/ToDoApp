from functions import *
import tkinter as tk
from tkinter import ttk

source_file = 'todo.txt'
# loading data from file
try:
    todo_list = get_todos(source_file)
except FileNotFoundError as error:
    print(error, "file with save todos is not present!")
    todos_list = []


window = tk.Tk()
window.title("ToDo App")
window.geometry("150x220")
window.resizable(0, 0)

todo_list_var = tk.Variable(value=todo_list)
entry_var = tk.StringVar()

frm_adding = tk.Frame(window)
lbl = ttk.Label(frm_adding, text="Insert your todo")
ent = ttk.Entry(frm_adding, textvariable=entry_var)
frm_list = tk.Frame(window)
listbox_todo = tk.Listbox(
    frm_list,
    listvariable=todo_list_var,
    height=6,
    selectmode=tk.SINGLE)



btn_add = ttk.Button(frm_adding, text="Add", command=lambda entry=ent, listbox=listbox_todo, todo_list=todo_list_var
                        : add_todos(entry, listbox, todo_list))
btn_edit = ttk.Button(frm_list, text="Edit", command=lambda entry=ent, listbox=listbox_todo, todo_list=todo_list_var
                        : edit_todos(entry, listbox, todo_list))
btn_complete = ttk.Button(frm_list, text="Complete", command=lambda entry=ent, listbox=listbox_todo, todo_list=todo_list_var
                        : delete_todos(entry, listbox, todo_list))

frm_adding.pack()
lbl.pack()
ent.pack()
btn_add.pack()
frm_list.pack()
listbox_todo.pack()
btn_edit.pack()
btn_complete.pack()

def items_selected(event):
    # get selected indices
    selected_indices = listbox_todo.curselection()
    ent.delete(0, END)
    ent.insert(0, todo_list_var.get()[selected_indices[0]])


listbox_todo.bind('<<ListboxSelect>>', items_selected)

window.mainloop()




