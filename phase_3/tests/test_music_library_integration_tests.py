from lib.music_library import *
from lib.track import *

def test_empty_library_initialises():
    ml = MusicLibrary()
    assert ml.tracks == []

def test_add_tracks_to_library():
    ml = MusicLibrary()
    ml = MusicLibrary()
    track_one = Track('American Idiot', 'Greenday')
    track_two = Track('One', 'Metalica')
    ml.add(track_one)
    ml.add(track_two)
    assert ml.tracks == [track_one, track_two]

def test_search_returns_match():
    ml = MusicLibrary()
    ml = MusicLibrary()
    track_one = Track('American Idiot', 'Greenday')
    track_two = Track('One', 'Metalica')
    ml.add(track_one)
    ml.add(track_two)
    assert ml.search('one') == [track_two]

def test_multiple_matches():
    ml = MusicLibrary()
    ml = MusicLibrary()
    track_one = Track('American Idiot', 'Greenday')
    track_two = Track('Basket Case', 'Greenday')
    ml.add(track_one)
    ml.add(track_two)
    assert ml.search('green') == [track_one, track_two]

def test_no_matches():
    ml = MusicLibrary()
    ml = MusicLibrary()
    track_one = Track('American Idiot', 'Greenday')
    track_two = Track('One', 'Metalica')
    ml.add(track_one)
    ml.add(track_two)
    assert ml.search('two') == []
