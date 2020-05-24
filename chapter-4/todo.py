#!/usr/bin/python3

def create_todo(todos, title, description, level):
    todo = {'title' : title,
            'description' : description,
            'level' : level }
    todos.append(todo)

def test(todos, abcd, ijkl):
    return "Command 'test' returned:\n" + \
    "abcd: " + abcd + "\nijkl: " + ijkl

def get_input(fields):
    user_input = {}
    for field in fields:
        user_input[field] = input(field+" > ")
    return user_input

def main_loop():
    user_input = ""
    while 1:
        print(run_command(user_input))
        user_input = input("> ")
        if user_input.lower().startswith("quit"):
            print("Exiting...")
            break;

def get_function(command_name):
    return commands[command_name]['function']

def get_fields(command_name):
    return commands[command_name]['fields']

def run_command(user_input, data=None):
    user_input = user_input.lower()
    if user_input not in commands:
        return user_input + "? I don't know what that command is."
    else:
        the_function = get_function(user_input)
    
    if data is None:
        the_fields = get_fields(user_input)
        data = get_input(the_fields)
    return the_function(todos, **data)


commands = {
    'new' : {'function' : create_todo, 'fields' : ['title', 'description', 'level']},
    'test' : {'function' : test, 'fields' : ['abcd', 'ijkl']},
    }

todos = []

if __name__ == '__main__':
    main_loop()

