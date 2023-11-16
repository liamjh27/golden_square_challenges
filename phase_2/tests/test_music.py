from lib.music import *

def test_music_initialises_with_empty_listened_to_list():
    music = Music()
    result = music.listened_to
    assert result == []

def test_add_music_to_listened_to_list():
    music = Music()
    music.add('Greenday', 'American Idiot')
    music.add('Bring Me The Horizon', 'Lost')
    result = music.listened_to
    assert result == ['Greenday - American Idiot', 'Bring Me The Horizon - Lost']

def test_add_music_to_listened_to_list_and_show():
    music = Music()
    music.add('Greenday', 'American Idiot')
    music.add('Bring Me The Horizon', 'Lost')
    result = music.show()
    assert result == ['Greenday - American Idiot', 'Bring Me The Horizon - Lost']