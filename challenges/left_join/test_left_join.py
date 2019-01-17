from .left_join import left_join
from ...data_structures.hash_table.hash_table import HashTable
import pytest


@pytest.fixture
def hashtable1():
    tmp = HashTable()
    data = [
        ('fond', 'enamored'),
        ('wrath', 'anger'),
        ('deligent', 'employed'),
        ('outfit', 'grab'),
        ]
    for pairs in data:
        tmp.put(pairs[0], pairs[1])
    return tmp


@pytest.fixture
def hashtable2():
    tmp = HashTable()
    data = [
        ('fond', 'averse'),
        ('wrath', 'delight'),
        ('deligent', 'idle'),
        ('flow', 'jam'),
        ]
    for pairs in data:
        tmp.put(pairs[0], pairs[1])
    return tmp


def test_import():
    assert left_join
    assert HashTable


def test_hashtable(hashtable1):
    tmp = hashtable1
    assert tmp.get('outfit') == 'grab'


def test_left_merge1(hashtable1, hashtable2):
    tmp = left_join(hashtable1, hashtable2)
    assert ['wrath', 'anger', 'delight'] in tmp
    assert ['outfit', 'grab', 'None'] in tmp


def test_left_merge2(hashtable1):
    tmp = left_join(hashtable1, HashTable())
    assert ['wrath', 'anger', 'None'] in tmp
    assert ['outfit', 'grab', 'None'] in tmp


def test_left_merge2(hashtable2):
    tmp = left_join(HashTable(), hashtable2)
    assert not tmp
