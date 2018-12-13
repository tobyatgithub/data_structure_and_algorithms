import pytest
from .multi_bracket_validation import multi_bracket_validation

@pytest.fixture()
def good_string1():
    return '%^&*()dasdaswe'

@pytest.fixture()
def good_string2():
    return '[({{([])}})]'

@pytest.fixture()
def good_string3():
    return '[][]()(){}{}()'

@pytest.fixture()
def bad_string1():
    return '((){{}[][]]]'

@pytest.fixture()
def bad_string2():
    return '[dsfewrsa}'

@pytest.fixture()
def bad_string3():
    return '[({)}]'

##########TESTING#######
def test_empty():
    assert multi_bracket_validation('')

def test_good1(good_string1):
    assert multi_bracket_validation(good_string1)

def test_good2(good_string2):
    assert multi_bracket_validation(good_string2)

def test_good3(good_string3):
    assert multi_bracket_validation(good_string3)

def test_bad1(bad_string1):
    assert not multi_bracket_validation(bad_string1)

def test_bad2(bad_string2):
    assert not multi_bracket_validation(bad_string2)

def test_bad3(bad_string3):
    assert not multi_bracket_validation(bad_string3)

def test_type_error():
    with pytest.raises(TypeError):
        multi_bracket_validation([1,2,3])
