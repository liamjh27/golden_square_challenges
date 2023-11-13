from lib.gratitudes import *

def test_starts_with_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add('dogs')
    gratitudes.add('chocolate')
    gratitudes.add('music')
    result = gratitudes.format()
    assert result == 'Be grateful for: dogs, chocolate, music'