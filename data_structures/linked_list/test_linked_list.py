from linked_list import linked_list
import pytest

@pytest.fixture
def empty_ll():
    return linked_list()

@pytest.fixture
def small_ll():
    ll = linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll

@pytest.fixture
def random_ll():
    from random import randint
    ll = linked_list()
    for i in range(100):
        ll.insert(randint(0,100))
    return ll

def test_ll_module_exists():
    assert linked_list

def test_ll_head_is_none(empty_ll):
    assert empty_ll.head is None


def test_ll_str_method(empty_ll):
    assert str(empty_ll) == f'Linked List: Head val - { empty_ll.head }'

def test_size_of_empty_ll(empty_ll):
    assert len(empty_ll) == 0

def test_small_fixture_has_size_of_4(small_ll):
    assert len(small_ll) == 4

def test_insert_new_node_into_empty(empty_ll):
    # test before
    assert empty_ll.head is None

    # do the thing,
    empty_ll.insert(1)

    # test after
    assert empty_ll.head.val == 1

def test_random_ll(random_ll):
    assert len(random_ll) == 100

def test_iterable_as_argument():
    ll = linked_list([1,2,3,4])
    assert ll.head.val == 4

def test_empty_includes(empty_ll):
    assert empty_ll.includes(233) == False

def test_includes1(small_ll):
    assert small_ll.includes(4) == True
    assert small_ll.includes(1) == True

def test_includes2(small_ll):
    assert small_ll.includes(5) == False
