import pytest
from .fifo_animal_shelter import AnimalShelter, dog, cat

@pytest.fixture()
def Jimmy():
    return dog(name = 'Jimmy', breed = 'Bull', color = 'black')

@pytest.fixture()
def Joe():
    return cat(name = 'Joe', kind = 'kattie', color = 'white')


@pytest.fixture()
def empty_shelter():
    return AnimalShelter()

@pytest.fixture()
def CCDD_shelter():
    tmp = AnimalShelter()
    tmp.enqueue(Joe)
    tmp.enqueue(Joe)
    tmp.enqueue(Jimmy)
    tmp.enqueue(Jimmy)
    return tmp


def test_shelter():
    assert AnimalShelter

def test_dog(Jimmy):
    assert Jimmy.val == 'dog'

def test_cat(Joe):
    assert Joe.val == 'cat'

def test_shelter1(empty_shelter):
    assert empty_shelter.front == None
    assert empty_shelter.back == None

# def test_shelter2(CCDD_shelter):
#     import pdb; pdb.set_trace()
#     assert CCDD_shelter.front.val.val == 'cat'
