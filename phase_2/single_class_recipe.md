Describe the problem:
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.
As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

Design the class interface

name Todo()
initialiser: empty list to store tasks
methods:
add(task):
task type = str
side effects: edits todo list
show_todo()
no parameters
side effects: none
returns list

mark_complete(task)
task type = str
side effects: edits todo list

create examples as tests:
seen in test_todo.py

implement the behaviour:
behaviour implemented 