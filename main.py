import functions
import tkinter as tk
from tkinter import ttk, Scrollbar
from tkinter import RIGHT, LEFT, BOTH


# loading data from file
todos_list = []
try:
    todo_list = functions.get_todos(functions.FILE_NAME)
except FileNotFoundError as error:
    print(error, "file with save todos is not present!")

window = tk.Tk()
window.title("ToDo App")
window.geometry("260x190")
window.resizable(False, False)

# variables
todo_list_var = tk.Variable(value=todo_list)
entry_var = tk.StringVar()

# structure - upper frame
frm_adding = tk.Frame(window)
lbl = ttk.Label(frm_adding, text="Insert your todo")
ent = ttk.Entry(frm_adding, textvariable=entry_var)
separator = ttk.Separator(window, orient='horizontal')

# structure - lower frame
frm_lower = tk.Frame(window)
frm_list = tk.Frame(frm_lower)
frm_buttons = tk.Frame(frm_lower)

# structure - Listbox control
scrollbar = Scrollbar(frm_list)
listbox_todo = tk.Listbox(
    frm_list,
    listvariable=todo_list_var,
    height=6,
    selectmode=tk.SINGLE)

listbox_todo.bind('<<ListboxSelect>>',
                  lambda event, entry=ent, listbox=listbox_todo, todos=todo_list_var:
                  functions.items_selected(event, entry, listbox, todos))
listbox_todo.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_todo.yview)

# structure - buttons
btn_add = ttk.Button(frm_buttons, text="Add",
                     command=lambda entry=ent, listbox=listbox_todo, todos=todo_list_var:
                     functions.add_todos(entry, listbox, todos))
btn_edit = ttk.Button(frm_buttons, text="Edit",
                      command=lambda entry=ent, listbox=listbox_todo, todos=todo_list_var:
                      functions.edit_todos(entry, listbox, todos))
btn_complete = ttk.Button(frm_buttons, text="Complete",
                          command=lambda entry=ent, listbox=listbox_todo, todos=todo_list_var:
                          functions.delete_todos(entry, listbox, todos))

# packing
frame_padding = {'pady': 5,
                 'padx': 5}
padding = {'pady': 3,
           'padx': 3}

# upper frame
frm_adding.pack(**frame_padding)
lbl.pack(**padding)
ent.pack(**padding)
btn_add.pack(**padding)
separator.pack(fill='x', **padding)

# lower frame
frm_lower.pack(**frame_padding)
frm_list.pack(side=LEFT)
scrollbar.pack(side=RIGHT, fill=BOTH, **padding)
listbox_todo.pack(side=LEFT, fill=BOTH, **padding)
frm_buttons.pack(side=LEFT)
btn_edit.pack(**padding)
btn_complete.pack(**padding)

window.mainloop()
