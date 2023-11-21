from lib.diary import * 

def test_diary_initiates_with_contents_and_reads_when_called():
    diary = Diary('Hello world, this is my diary!')
    assert diary.read() == 'Hello world, this is my diary!'