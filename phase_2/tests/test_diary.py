from lib.diary import *
from lib.diary_entry_class import *

def test_entries_can_be_added_and_shown():
    diary = Diary()
    first_entry = DiaryEntry('Beginning', 'This is my first entry.')
    second_entry = DiaryEntry('Middle', 'This is the middle entry')
    third_entry = DiaryEntry('End', 'This is my final entry.')
    diary.add(first_entry)
    diary.add(second_entry)
    diary.add(third_entry)
    result = diary.all()
    assert result == [first_entry, second_entry, third_entry]

def test_count_words_returns_total_for_all_entries():
    diary = Diary()
    first_entry = DiaryEntry('Beginning', 'This is my first entry.')
    second_entry = DiaryEntry('Middle', 'This is the middle entry')
    third_entry = DiaryEntry('End', 'This is my final entry.')
    diary.add(first_entry)
    diary.add(second_entry)
    diary.add(third_entry)
    result = diary.count_words_total()
    assert result == 15

def test_reading_time_total_for_all_entries():
    diary = Diary()
    first_entry = DiaryEntry('Beginning', 'This is my first entry.')
    second_entry = DiaryEntry('Middle', 'This is the middle entry')
    third_entry = DiaryEntry('End', 'This is my final entry.')
    diary.add(first_entry)
    diary.add(second_entry)
    diary.add(third_entry)
    result = diary.reading_time(5)
    assert result == 3
    
def test_best_entry_for_reading_time():
    diary = Diary()
    first_entry = DiaryEntry('Beginning', 'This is my first entry.')
    second_entry = DiaryEntry('Middle', 'This is the middle entry. Here is another five words.')
    third_entry = DiaryEntry('End', 'This is my final entry. Ten more words here will make this diary entry longer.')
    diary.add(first_entry)
    diary.add(second_entry)
    diary.add(third_entry)
    result = diary.best_entry_for_reading_time(5, 2)
    assert result == second_entry