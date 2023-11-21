from lib.music_library import *
from unittest.mock import Mock

def test_empty_library_initialises():
    ml = MusicLibrary()
    assert ml.tracks == []

def test_add_tracks_to_library():
    ml = MusicLibrary()
    ml = MusicLibrary()
    track_one = Mock()
    track_one.title = 'American Idiot'
    track_one.artist = 'Greenday'
    track_two = Mock()
    track_two.title = 'One'
    track_two.artist = 'Metalica'
    ml.add(track_one)
    ml.add(track_two)
    assert ml.tracks == [track_one, track_two]

def test_search_returns_match():
    ml = MusicLibrary()
    track_one = Mock()
    track_one.title = 'American Idiot'
    track_one.artist = 'Greenday'
    track_two = Mock()
    track_two.title = 'One'
    track_two.artist = 'Metalica'
    track_one.matches.return_value = False
    track_two.matches.return_value = True
    ml.add(track_one)
    ml.add(track_two)
    assert ml.search('one') == [track_two]

def test_multiple_matches():
    ml = MusicLibrary()
    ml = MusicLibrary()
    track_one = Mock()
    track_two = Mock()
    track_one.matches.return_value = True
    track_two.matches.return_value = True
    ml.add(track_one)
    ml.add(track_two)
    assert ml.search('green') == [track_one, track_two]

def test_no_matches():
    ml = MusicLibrary()
    track_one = Mock()
    track_two = Mock()
    track_one.matches.return_value = False
    track_two.matches.return_value = False
    ml.add(track_one)
    ml.add(track_two)
    assert ml.search('two') == []
