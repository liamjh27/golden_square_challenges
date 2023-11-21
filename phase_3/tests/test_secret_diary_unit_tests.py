from lib.secret_diary import *
from unittest.mock import Mock

def test_diary_is_locked_and_does_not_read_on_start_up():
    diary= Mock()
    sd = SecretDiary(diary)
    assert sd.locked
    assert sd.read() == 'Go away!'

def test_unlock_diary_will_allow_reading():
    diary = Mock()
    sd = SecretDiary(diary)
    diary.read.return_value = 'Hello world'
    sd.unlock()
    assert sd.locked == False
    assert sd.read() == 'Hello world'

    