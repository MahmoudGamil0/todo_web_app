import streamlit as st
from files.functions import *

todos = get_todo()

st.set_page_config(layout = "wide")

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    write_todo(todos)

st.title('My ToDo App')
st.write("This app will increase nothing")

st.text_input(label = '', placeholder = 'Add New ToDo',
              on_change = add_todo, key = 'new_todo')

for index, todo in enumerate(todos):
    check =  st.checkbox(todo, key = todo)
    if check:
        todos.pop(index)
        write_todo(todos)
        del st.session_state[todo]
        st.rerun()
