FILE_PATH = r"./mount/src/web_app1//todos.txt"

def get_todos(filepath=FILE_PATH): #make the parameter/argument default
    """Read the text file and return the list of todos""" #this is a doc string, used for documentation
    #if someone runs a help function, this will show up such as print(help(get_todos))
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILE_PATH): #order matters and it's better to have the nondefault parameter
    #first. So we switched it so that todos_arg is first.
    """Write todos item list to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":

    print("Hello from the function")
    print(get_todos())