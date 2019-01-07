import pytest
from .kth_smallest_bst import BST

@pytest.fixture
def small_tree():
    return BST([2,1,3,4,5])

@pytest.fixture
def mid_tree():
    return BST([23,44,90,22,11,46,99,250])

def test_kth_smallest_exist():
    tmp = BST()
    assert not tmp.kth_Smallest(2)

def test_kth_smallest1(small_tree):
    assert small_tree.kth_Smallest(2) == 2
    assert small_tree.kth_Smallest(1) == 1

def test_kth_smallest2(mid_tree):
    assert mid_tree.kth_Smallest(8) == 250
