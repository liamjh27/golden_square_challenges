from lib.present import *
import pytest 


def test_unwrap_error():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    errormessage = str(e.value)
    assert errormessage == 'No contents have been wrapped.'

def test_multiple_wrapping_error():
    present = Present()
    present.wrap('gift')
    with pytest.raises(Exception) as e:
        present.wrap('more gifts')
    error_message = str(e.value)
    assert error_message == 'A contents has already been wrapped.'

def test_unwrapping_works():
    present = Present()
    present.wrap('gift')
    result = present.unwrap()
    assert result == 'gift'