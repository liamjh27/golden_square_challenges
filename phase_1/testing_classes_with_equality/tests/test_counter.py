from lib.counter import *

def test_counter_starts_at_zero():
    counter = Counter()
    result = counter.report()
    assert result == 'Counted to 0 so far.'

def test_counter_counts_to_ten():
    counter = Counter()
    counter.add(6)
    counter.add(4)
    result = counter.report()
    assert result == 'Counted to 10 so far.'