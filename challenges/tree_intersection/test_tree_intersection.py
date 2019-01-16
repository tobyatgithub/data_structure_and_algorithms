from ...data_structures.binary_search_tree.bst import BST
from .tree_intersection import tree_intersection
import pytest


def test_import():
    assert BST
    assert tree_intersection


def test_intersection():
    Tree1 = BST([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    Tree2 = BST()
    assert not tree_intersection(Tree1, Tree2)


def test_intersection1():
    Tree1 = BST()
    Tree2 = BST()
    assert not tree_intersection(Tree1, Tree2)


def test_intersection2():
    Tree1 = BST([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    Tree2 = BST([5, 7, 9, 17, 19, 22, 24, 18, 20])
    assert set([19, 18, 22, 20]) == tree_intersection(Tree1, Tree2)

