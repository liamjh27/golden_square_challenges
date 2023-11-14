from lib.personal_diary import *
import pytest 

def test_make_snippet_returns_shortened_entry():
    result = make_snippet('This will cut off here and this won\'t be shown')
    assert result == 'This will cut off here...'

def test_short_snippet_shows_all():
    result = make_snippet('This is short')
    assert result == 'This is short'

def test_count_words_returns_three():
    result = count_words('this is three.')
    assert result == 3

def test_count_words_with_ten_words():
    result = count_words('this string has ten words in it at the end.')
    assert result == 10

def test_three_hundred_words_returns_one_point_five():
    inputstring = []
    for i in range(300):
        inputstring.append('word')
    inputstring = ' '.join(inputstring)
    result = estimate_reading_time(inputstring)
    assert result == 1.5

def test_seven_hundred_words_returns_three_point_five():
    inputstring = []
    for i in range(700):
        inputstring.append('word')
    inputstring = ' '.join(inputstring)
    result = estimate_reading_time(inputstring)
    assert result == 3.5


def test_check_sentence_grammar_without_capital():
    result = check_sentence_grammar('this will not pass!')
    assert result == False

def test_check_sentence_grammar_passes_with_question():
    result = check_sentence_grammar('Will this pass?')
    assert result == True 

def test_test_check_sentence_fails_without_ending_punctuation():
    result = check_sentence_grammar('This will not pass')
    assert result == False 

def test_check_sentence_grammar_passes_with_proper_sentence():
    result = check_sentence_grammar('This is a sentence and it will pass.')
    assert result == True

def test_check_contains_todo_errors_when_not_string():
    with pytest.raises(Exception) as e:
        check_contains_todo(['this', 'will', 'fail'])
    error_message = str(e.value)
    assert error_message == 'Input must be string'

def test_check_contains_todo_returns_false_without_todo():
    result = check_contains_todo('this string does not contain the keywords so should not return true.')
    assert result == False

def test_check_contains_todo_returns_true_with_todo_in_text():
    result = check_contains_todo('this text will return true because it contains #TODO. That is the theory at least.')
    assert result == True


def test_check_contians_todo__returns_false_when_todo_is_lowercase():
    result = check_contains_todo('this should return false #todo because it is lower case.')
    assert result == False 

def test_check_contains_todo_returns_true_with_todo_at_start():
    result = check_contains_todo('#TODO update files to say they are done.')
    assert result == True 

