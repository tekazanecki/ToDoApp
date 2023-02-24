import streamlit as st
import functions

todos = functions.get_todos(functions.FILE_NAME)


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo)
    functions.save_todos(todos)

def delete_todo(idx):
    todos.pop(idx)
    functions.save_todos(todos)
    del st.session_state[idx]
    st.experimental_rerun()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=idx)
    if checkbox:
        delete_todo(idx)


st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

st.session_state