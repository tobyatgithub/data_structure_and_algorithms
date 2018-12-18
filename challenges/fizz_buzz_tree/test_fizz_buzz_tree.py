import pytest
from ...data_structures.binary_search_tree.bst import BST
from .fizz_buzz_tree import fizzit, FizzBuzzTree

# test all kinds of input for fizzit
def test_fizzit():
    assert fizzit(5) == "Buzz"
    assert fizzit(15) == "FizzBuzz"
    assert fizzit(3) == "Fizz"
    assert fizzit(22) == 22
    with pytest.raises(TypeError):
        fizzit("15")

@pytest.fixture()
def a_tree():
    return BST([14,5,9,30])

@pytest.fixture()
def b_tree():
    return BST([20, 18, 12, 19, 11, 15, 40, 31, 22, 33])

@pytest.fixture()
def c_tree():
    return BST()

def test_fizz_buzz_tree(a_tree):
    tmp = FizzBuzzTree(a_tree)
    assert tmp.root.val == 14
    assert tmp.root.left.val == "Buzz"
    assert tmp.root.right.val == "FizzBuzz"
    assert tmp.root.left.right.val == "Fizz"

def test_fizz_buzz_tree2(b_tree):
    tmp = FizzBuzzTree(b_tree)
    assert tmp.root.val == "Buzz"
    assert tmp.root.left.left.right.val == "FizzBuzz"
    assert tmp.root.right.left.right.val == "Fizz"
    assert tmp.root.right.left.val == 31

def test_fizz_buzz_tree3(c_tree):
    tmp = FizzBuzzTree(c_tree)
    assert tmp.root == None
