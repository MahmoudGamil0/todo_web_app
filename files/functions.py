file_path = 'files/todo.txt'

def get_todo(filepath = file_path):
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todo(todos_local, filepath = file_path):
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_local)

