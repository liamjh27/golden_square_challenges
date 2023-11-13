from lib.password_checker import *
import pytest 

def test_short_password_fails():
    pw = PasswordChecker()
    with pytest.raises(Exception) as e:
        pw.check('short')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_long_password_passes():
    pw = PasswordChecker()
    result = pw.check('longpassword')
    assert result == True

def test_eight_characters_passes():
    pw = PasswordChecker()
    result = pw.check('88888888')
    assert result == True