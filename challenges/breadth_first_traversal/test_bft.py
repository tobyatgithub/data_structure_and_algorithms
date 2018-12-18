from .breadth_first_traversal import breadth_first_traversal
from ...data_structures.binary_search_tree.bst import BST
import pytest

@pytest.fixture()
def a_tree():
    return BST([14,5,9,30])

@pytest.fixture()
def b_tree():
    return BST([20, 18, 12, 19, 11, 15, 40, 31, 22, 33])

def test_bft1(capsys):
    a_tree = BST([14,5,9,30])
    tmp = breadth_first_traversal(a_tree)
    captured = capsys.readouterr()
    # import pdb; pdb.set_trace()
    assert captured.out == "14\n5\n30\n9\n"
    # assert True

def test_bft2(capsys):
    tmp = BST()
    captured = capsys.readouterr()
    assert captured.out == ""

def test_bft3(capsys):
    tmp = BST([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    breadth_first_traversal(tmp)
    captured = capsys.readouterr()
    assert captured.out == "20\n18\n40\n12\n19\n31\n11\n14\n22\n33\n"
