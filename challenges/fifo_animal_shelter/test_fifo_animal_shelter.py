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
def CD_shelter(Joe, Jimmy):
    tmp = AnimalShelter()
    tmp.enqueue(Joe)
    tmp.enqueue(Jimmy)
    return tmp

@pytest.fixture()
def mid_shelter(Joe, Jimmy):
    # cat-cat-dog-cat-dog-dog
    tmp = AnimalShelter()
    tmp.enqueue(Joe)
    tmp.enqueue(Joe)
    tmp.enqueue(Jimmy)
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

def test_shelter2(CD_shelter):
    assert CD_shelter.front.val.val == 'cat'

def test_shelter3(CD_shelter):
    assert CD_shelter.front._next.val.val == 'dog'

def test_dequeue(mid_shelter, Joe, Jimmy):
    tmp = mid_shelter.dequeue('cat')
    assert tmp.val.val == Joe.val


def test_dequeue2(mid_shelter, Joe, Jimmy):
    # tmp = mid_shelter.dequeue('cat')
    tmp = mid_shelter.dequeue('dog')
    # import pdb; pdb.set_trace()
    assert tmp.val.val == Jimmy.val

def test_dequeue3(empty_shelter):
    assert not empty_shelter.dequeue('cat')
    assert not empty_shelter.dequeue('dog')
