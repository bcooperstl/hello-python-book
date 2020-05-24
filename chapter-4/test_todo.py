#!/usr/bin/python3

import todo

def test_get_function():
    assert todo.get_function('new') == todo.create_todo
    print("OK - get_function")

def test_get_fields():
    assert (todo.get_fields('new') == ['title', 'description', 'level'])
    print("OK - get_fields")

def test_run_command():
    result = todo.run_command('test', {'abcd':'efgh', 'ijkl':'mnop'})
    expected = """Command 'test' returned:
abcd: efgh
ijkl: mnop"""
    assert result == expected, result + " != " + expected
    print("OK - run_command")

def test_create_todo():
    todo.todos = []
    todo.create_todo(todo.todos,
        title="Make some stuff",
        description="Stuff needs to be programmed",
        level="Important")
    
    assert len(todo.todos) == 1, "Todo was not created!"
    assert todo.todos[0]['title'] == "Make some stuff"
    assert todo.todos[0]['description'] == "Stuff needs to be programmed"
    assert todo.todos[0]['level'] == "Important"
    
    print("OK - create_todo")

def test_show_todos():
    todo.todos = [
        { 'title' : 'test todo',
          'description' : 'This is a test',
          'level' : 'Important'
        }
    ]
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")
    
    title_line = lines[0]
    assert "Item" in title_line
    assert "Title" in title_line
    assert "Description" in title_line
    assert "Level" in title_line
    
    values_line = lines[1]
    assert "1" in values_line
    assert "test todo" in values_line
    assert "This is a test" in values_line
    assert "Important" in values_line
    
    print("OK - show_todos")
    

test_get_function()
test_get_fields()
test_run_command()
test_create_todo()
test_show_todos()
