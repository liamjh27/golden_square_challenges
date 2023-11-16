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


Describe the problem:
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

design the class interface:
classname music
initialise with attributes:
empty list called listened_to to track songs that have been listened to.

methods:
add() to add songs listened to to the listened_to list.
paramaters:
artist type:str
song type:str
side effects: adds to the listened_to list

show() to show list of listened to music.
parameters: none
side effects: none