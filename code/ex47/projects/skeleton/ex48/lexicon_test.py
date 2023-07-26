from nose.tools import *
from ex48 import lexicon
import lexicon
from typing import List, Tuple
from nose.tools import assert_equal

'''def test_directions():
    pass'''

def test_directions() -> None:
    assert_equal(lexicon.scan("north"), [('direction', 'north')])

    result: List[Tuple[str, str]] = lexicon.scan("north south east")
    expected_result: List[Tuple[str, str]] = [('direction', 'north'),
                                              ('direction', 'south'),
                                              ('direction', 'east')]
    assert_equal(result, expected_result)
                        
def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                        ('verb', 'kill'),
                        ('verb', 'eat')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")    
    assert_equal(result, [('stop', 'the'),
                        ('stop', 'in'),
                        ('stop', 'of')])


def test_nouns() -> None:
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                        ('number', 91234)])


def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"),
                        [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                        ('error', 'IAS'),
                        ('noun', 'princess')])


# nosetests lexicon_tests.py