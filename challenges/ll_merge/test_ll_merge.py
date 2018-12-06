import pytest
from ll_merge import mergeLists

import sys
sys.path.append('/Users/toby/Documents/seattle-python-401d10/data_structure_and_algorithms/data_structures/linked_list')
from linked_list import linked_list
from node import Node

@pytest.fixture(scope = "function")
def empty_ll1():
    return linked_list()

@pytest.fixture(scope = "function")
def empty_ll2():
    return linked_list()


@pytest.fixture(scope = "function")
def small_ll():
    ll = linked_list([1,2,3,4][::-1])
    # ll.insert(1)
    # ll.insert(2)
    # ll.insert(3)
    # ll.insert(4)
    return ll

@pytest.fixture(scope = "function")
def small_string_ll():
    ll = linked_list(['a','b','c','d'][::-1])
    # ll.insert("a")
    # ll.insert("b")
    # ll.insert("c")
    # ll.insert("d")
    return ll

@pytest.fixture(scope = "function")
def long_ll():
    ll = linked_list([1,2,3,4,5,6,7][::-1])
    # ll.insert(1)
    # ll.insert(2)
    # ll.insert(3)
    # ll.insert(4)
    # ll.insert(5)
    # ll.insert(6)
    # ll.insert(7)
    return ll

@pytest.fixture(scope = "function")
def long_string_ll():
    ll = linked_list(['a','b','c','d','e','f','g'][::-1])
    # ll.insert("a")
    # ll.insert("b")
    # ll.insert("c")
    # ll.insert("d")
    # ll.insert("e")
    # ll.insert("f")
    # ll.insert("g")
    return ll


# test exist and it merges two empty correctly
def test_empty_empty_merge(empty_ll1, empty_ll2):
    response = mergeLists(empty_ll1, empty_ll2)
    assert response == None

# test merge when one input is empty
def test_part_empty_merge1(small_ll, empty_ll1):
    response = mergeLists(small_ll, empty_ll1) # this returns a ref of new_ll head
    assert response.val == small_ll.head.val
    assert response == small_ll.head

def test_part_empty_merge2(empty_ll2, small_ll):
    response = mergeLists(empty_ll2, small_ll) # this returns a ref of new_ll head
    assert response.val == small_ll.head.val
    assert response == small_ll.head

# test merge for input lists with equal length.
def test_equal_length_merge1(small_ll, small_string_ll):
    response = mergeLists(small_ll, small_string_ll) # this returns a ref of new_ll head
    # assert response.val == small_ll.head._next._next._next.val
    # print("response  = ", response.val)
    # assert type(response) == Node
    # assert type(response.val) == int
    # assert True == True
    assert response.val == None
    assert response._next.val == 1
    assert response._next._next.val == 'a'

def test_equal_length_merge2(small_ll, small_string_ll):
    response = mergeLists(small_string_ll, small_ll) # this returns a ref of new_ll head
    assert response.val == None
    assert response._next.val == 'a'
    assert response._next._next.val == 1
    assert response._next._next._next.val == 'b'

def test_diff_length_merge1(small_ll, long_ll):
    response = mergeLists(small_ll, long_ll)
    assert response.val == None
    assert response._next.val == 1
    assert response._next._next.val == 1

def test_diff_length_merge2(small_ll, long_string_ll):
    response = mergeLists(small_ll, long_string_ll)
    assert response.val == None
    assert response._next.val == 1
    assert response._next._next.val == 'a'
    assert response._next._next._next.val == 2
