from lib.todo import *

def test_initialises_with_empty_list():
    todo = Todo()
    result = todo.todo_list
    assert result == [] 

def test_add_todo_item():
    todo = Todo()
    todo.add('Test class')
    result = todo.todo_list
    assert result == ['Test class']

def test_show_todo_list():
    todo = Todo()
    todo.add('Test class')
    result = todo.show_todo()
    assert result == ['Test class']

def test_mark_complete_removes_from_list():
    todo = Todo()
    todo.add('Test class')
    todo.add('Add something to remove')
    todo.mark_complete('Add something to remove')
    result = todo.show_todo()
    assert result == ['Test class']