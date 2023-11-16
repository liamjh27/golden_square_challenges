from lib.todo_list import *
from lib.todo_item import * 

def test_can_add_tasks_to_todo_list():
    tasks = Todo()
    task_one = Task('Buy food')
    task_two = Task('Buy drinks')
    tasks.add(task_one)
    tasks.add(task_two)
    result = tasks.task_list
    assert result == [task_one, task_two]

def test_complete_shows_completed_items():
    tasks = Todo()
    task_one = Task('Buy food')
    task_two = Task('Buy drinks')
    tasks.add(task_one)
    tasks.add(task_two)
    task_one.mark_complete()
    result = tasks.complete()
    assert result == [task_one]

def test_incomplete_shows_incomplete_items():
    tasks = Todo()
    task_one = Task('Buy food')
    task_two = Task('Buy drinks')
    tasks.add(task_one)
    tasks.add(task_two)
    task_two.mark_complete()
    result = tasks.incomplete()
    assert result == [task_one]

def test_give_up_marks_all_complete():
    tasks = Todo()
    task_one = Task('Buy food')
    task_two = Task('Buy drinks')
    tasks.add(task_one)
    tasks.add(task_two)
    tasks.give_up()
    result = tasks.complete()
    assert result == [task_one, task_two]