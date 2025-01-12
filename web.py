import streamlit as sl
from modules import functions

sl.title("Todo App")
todos = functions.get_todos()
print("test")

def add_todo():
    todo = sl.session_state["add_todo"]
    if not todo == "" and not todo.isspace():
        todos.append(todo + "\n")
        functions.write_todos(todos)


for index,todo in enumerate(todos):
    checkbox = sl.checkbox(todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # stop the rest of the script and rerun the whole script
        sl.rerun()

sl.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="add_todo")

