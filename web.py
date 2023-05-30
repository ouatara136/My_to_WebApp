import streamlit as st
import functions

todos = functions.getTodos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.writeTodos(todos)


st.title("My Todo Web App")
st.subheader("This is my first web app")
st.text("Now, your productivity will be increased")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.writeTodos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="Enter a new todo", label_visibility="hidden", placeholder="Enter a todo", key="new_todo",
              on_change=add_todo)

# st.session_state