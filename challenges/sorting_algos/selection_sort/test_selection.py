from .selection import selection_sort
from random import shuffle


def test_import():
    assert selection_sort


def test_sele_sort1():
    tmp = selection_sort([1, 2, 3, 4, 5])
    assert [1, 2, 3, 4, 5] == tmp


def test_sele_sort2():
    tmp = selection_sort([5, 4, 3, 2, 1])
    assert [1, 2, 3, 4, 5] == tmp


def test_sele_sort3():
    tmp = selection_sort([])
    assert [] == tmp


def test_sele_sort4():
    tmp = selection_sort([1, 1, 1, 1, 1])
    assert [1, 1, 1, 1, 1] == tmp


def test_sele_sort5():
    for _ in range(10):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shuffle(a)
        tmp = selection_sort(a)
        assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == tmp
