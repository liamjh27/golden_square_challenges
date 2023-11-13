from lib.check_codeword import * 

def test_that_house_caps_is_wrong():
    result = check_codeword('HOUSE')
    assert result == 'WRONG!'

def test_house_is_close():
    result = check_codeword('house')
    assert result == 'Close, but nope.'

def test_check_horse_is_correct():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'