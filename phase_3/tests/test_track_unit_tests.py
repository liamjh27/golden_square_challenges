from lib.track import *

def test_title():
    track = Track('American Idiot', 'Greenday')
    assert track.title == 'American Idiot'

def test_artist():
    track = Track('American Idiot', 'Greenday')
    assert track.artist == 'Greenday'

def test_keyword_match_green():
    track = Track('American Idiot', 'Greenday')
    assert track.matches('Green') == True

def test_matches_title():
    track = Track('American Idiot', 'Greenday')
    assert track.matches('Idiot') == True

def test_matches_fails_with_no_match():
    track = Track('American Idiot', 'Greenday')
    assert track.matches('blue') == False