#!/usr/bin/python3

def create_todo(todos, title, description, level):
    todo = {'title' : title,
            'description' : description,
            'level' : level }
    todos.append(todo)

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

commands = {
    'new' : {'function' : create_todo, 'fields' : ['title', 'description', 'level']}
    }

if __name__ == '__main__':
    main_loop()
