import streamlit as st
from files.functions import *

todos = get_todo()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    write_todo(todos)

st.title('My ToDo App')
st.subheader("This is my shit")
st.write("This app is to increase your shit, mf")

for index, todo in enumerate(todos):
    check =  st.checkbox(todo, key = todo)
    if check:
        todos.pop(index)
        write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = '', placeholder = 'Add new ToDo',
              on_change = add_todo, key = 'new_todo')
