from lib.diary import *
from lib.diary_entry_class import *
from lib.todo_item import *
from lib.todo_list import *


def test_entry_title():
    diary = Diary()
    entry = DiaryEntry('First entry', 'Contents of first entry.')
    check_title = entry.title
    assert check_title == 'First entry'

def test_entry_contents():
    diary = Diary()
    entry = DiaryEntry('First entry', 'Contents of first entry.')
    check_contents = entry.contents
    assert check_contents == 'Contents of first entry.'

def test_create_diary_and_diary_entry_then_read_entry():
    diary = Diary()
    entry = DiaryEntry('First entry', 'Contents of first entry')
    entry_two = DiaryEntry('Second entry', 'Contents of second entry.')
    diary.add(entry)
    diary.add(entry_two)
    result = diary.read(entry_two)
    assert result == 'Second entry : Contents of second entry.'

def test_best_entry_for_reading_time():
    diary = Diary()
    first_entry = DiaryEntry('One', 'word word word word word')
    second_entry = DiaryEntry('two', 'word word word word word word word word word word word word word word word')
    third_entry = DiaryEntry('three', 'word word word word word word word word word word')
    diary.add(first_entry)
    diary.add(second_entry)
    diary.add(third_entry)
    result = diary.best_entry_for_reading_time(5, 2)
    assert result == third_entry

def test_find_mobile_numbers():
    diary = Diary()
    first_entry = DiaryEntry('Number here', 'This entry contains a mobile number. it is 07777777777.')
    second_entry = DiaryEntry('second', 'nothing important here.')
    third_entry = DiaryEntry('third', 'My new number is 07111111111 and works from today.')
    diary.add(first_entry)
    diary.add(second_entry)
    diary.add(third_entry)
    result = diary.get_numbers()
    assert result == ['07777777777', '07111111111']


# begins tests for todo list

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