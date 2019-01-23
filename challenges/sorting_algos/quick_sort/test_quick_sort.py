from .quick_sort import quick_sort
from random import shuffle


def test_import():
    assert quick_sort


def test_quick_sort1():
    tmp = [1, 2, 3, 4, 5]
    quick_sort(tmp, 0, 5)
    assert [1, 2, 3, 4, 5] == tmp


def test_quick_sort2():
    tmp = [5, 4, 3, 2, 1]
    quick_sort(tmp, 0, 5)
    assert [1, 2, 3, 4, 5] == tmp


def test_quick_sort3():
    tmp = []
    quick_sort(tmp, 0, 0)
    assert [] == tmp


def test_quick_sort4():
    tmp = [1, 1, 1, 1, 1]
    quick_sort(tmp, 0, 5)
    assert [1, 1, 1, 1, 1] == tmp


def test_quick_sort5():
    for _ in range(10):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shuffle(a)
        quick_sort(a, 0, len(a))
        assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == a
    a = [7, 6, 1, 2, 10, 9, 4, 8, 3, 5]
    quick_sort(a, 0, len(a))
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == a
