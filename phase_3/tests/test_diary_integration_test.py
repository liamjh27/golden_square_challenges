from lib.diary import *
from lib.secret_diary import *

def test_read_contents_of_locked_diary_fails():
    diary = Diary('Hello world')
    sd = SecretDiary(diary)
    assert sd.read() == 'Go away!'

def test_unlocked_diary_reads():
    diary = Diary('Hello world')
    sd = SecretDiary(diary)
    sd.unlock()
    assert sd.read() == 'Hello world'

def test_unlock_and_relock_diary():
    diary = Diary('Hello world')
    sd = SecretDiary(diary)
    sd.unlock()
    assert sd.read() == 'Hello world'
    sd.lock()
    assert sd.read() == 'Go away!'