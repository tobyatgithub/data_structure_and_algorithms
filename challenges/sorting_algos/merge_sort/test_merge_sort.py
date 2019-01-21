from .merge_sort import merge_sort
from random import shuffle


def test_input():
    assert merge_sort


def test_merge_sort1():
    tmp = merge_sort([1, 2, 3, 4, 5])
    assert [1, 2, 3, 4, 5] == tmp


def test_merge_sort2():
    tmp = merge_sort([5, 4, 3, 2, 1])
    assert [1, 2, 3, 4, 5] == tmp


def test_merge_sort3():
    tmp = merge_sort([])
    assert [] == tmp


def test_merge_sort4():
    tmp = merge_sort([1, 1, 1, 1, 1])
    assert [1, 1, 1, 1, 1] == tmp


def test_merge_sort5():
    for _ in range(10):
        a = [-10, -5, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shuffle(a)
        tmp = merge_sort(a)
        assert [-10, -5, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == tmp
