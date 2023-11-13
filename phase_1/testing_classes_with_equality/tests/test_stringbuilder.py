from lib.stringbuilder import *

def test_starts_with_empty_string():
    sb = StringBuilder()
    result = sb.output()
    assert result == ''

def test_stringbuilder_and_size():
    sb = StringBuilder()
    sb.add('This ')
    sb.add('is ')
    sb.add('10')
    result = sb.size()
    assert result == 10

def test_combination_of_methods():
    string = StringBuilder()
    string.add('This is 10')
    result = f'{string.output()} was {string.size()} characters long'
    assert result == 'This is 10 was 10 characters long'
