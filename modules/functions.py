FILEPATH="todo.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todo_list_local = file_local.readlines()
        return todo_list_local


def write_todos(todo_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)


"""

# Execute when we run functions.py directly.
if __name__ == "__main__":
    print("Running from main script")

# Execute when we import function.py in another python script then we run that script
if __name__ == "modules.functions": 
    print("Running from another script ")

"""