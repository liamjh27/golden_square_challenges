from lib.cat_facts import * 
from unittest.mock import Mock


def test_cat_facts():
    mockreq = Mock(name='request')
    mockres = Mock(name='response')
    mockreq.get.return_value = mockres
    mockres.json.return_value = {"fact":"Cats only use their meows to talk to humans, not each other. The only time they meow to communicate with other felines is when they are kittens to signal to their mother.","length":170}

    cf = CatFacts(mockreq)
    assert cf.provide() == "Cat fact: Cats only use their meows to talk to humans, not each other. The only time they meow to communicate with other felines is when they are kittens to signal to their mother."