FILEPATH = "todos.txt"
def getTodos(filepath=FILEPATH):
    """open and read a text file and return the list of the to-do items"""
    with open(filepath, 'r') as localFile:
        localTodos = localFile.readlines()
        return localTodos


def writeTodos(todosArg, filepath=FILEPATH):
    """open and write the to-do item list in a text file"""

    with open(filepath, 'w') as file:
        file.writelines(todosArg)