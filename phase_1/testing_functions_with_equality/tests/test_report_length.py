from lib.report_length import *

def test_string_is_ten_characters():
    result = report_length('This is 10')
    assert result == 'This string was 10 characters long.'

def test_this_string_returns_forty_four():
    result = report_length('This is a much longer string and is 44 long.')
    assert result == 'This string was 44 characters long.'

def test_special_characters_returns_eight():
    result = report_length('!@£$%^&*')
    assert result == 'This string was 8 characters long.'