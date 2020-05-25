#!/usr/bin/python3

import textwrap

def create_todo(todos, title, description, level):
    todo = {'title' : title,
            'description' : description,
            'level' : level }
    todos.append(todo)

def capitalize_level(todo):
    todo['level'] = todo['level'].upper()
    return todo

def show_todo(todo, index):
    wrapped_title = textwrap.wrap(todo['title'], 16)
    wrapped_description = textwrap.wrap(todo['description'], 24)
    
    output = str(index+1).ljust(8) + "  "
    output += wrapped_title[0].ljust(16) + "  "
    output += wrapped_description[0].ljust(24) + "  "
    output += todo['level'].ljust(16)
    output += "\n"
    
    max_len = max(len(wrapped_title), len(wrapped_description))
    for index in range(1, max_len):
        output += " " * 8 + "  " # no index needed
        if index < len(wrapped_title):
            output += wrapped_title[index].ljust(16) + "  "
        else:
            output += " " * 16 + "  "
        if index < len(wrapped_description):
            output += wrapped_description[index].ljust(24) + "  "
        else:
            output += " " * 24 + "  "
        output += "\n"
    return output

def sort_todos(todos):
    important = [capitalize_level(todo) for todo in todos
                 if todo['level'].lower() == 'important']
    unimportant = [todo for todo in todos
                   if todo['level'].lower() == 'unimportant']
    medium = [todo for todo in todos
              if todo['level'].lower() not in ['important', 'unimportant']]
    todos = (important + medium + unimportant)
    return todos
    
def show_todos(todos):
    output = ("Item      Title             "
              "Description               Level\n")
    sorted_todos = sort_todos(todos)
    for index, todo in enumerate(sorted_todos):
        output += show_todo(todo, index)
    return output
    
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
    'show' : {'function' : show_todos, 'fields' : []},
    'test' : {'function' : test, 'fields' : ['abcd', 'ijkl']},
    }

todos = []

if __name__ == '__main__':
    main_loop()

