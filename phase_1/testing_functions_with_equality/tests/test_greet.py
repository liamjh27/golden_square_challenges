from lib.greet import * 

def test_greet_bob_greets_bob():
    result = greet('Bob')
    assert result == 'Hello, Bob!'

def test_greet_liam_greets_liam():
    result = greet('Liam')
    assert result == 'Hello, Liam!'