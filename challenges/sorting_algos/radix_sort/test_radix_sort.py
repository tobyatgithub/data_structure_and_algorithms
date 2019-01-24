from .radix_sort import radix_sort
# from random import shuffle
import random


def test_import():
    assert radix_sort


def test_radix_sort1():
    tmp = radix_sort([1, 2, 3, 4, 5])
    assert [1, 2, 3, 4, 5] == tmp


def test_radix_sort2():
    tmp = radix_sort([5, 4, 3, 2, 1])
    assert [1, 2, 3, 4, 5] == tmp


def test_radix_sort3():
    tmp = radix_sort([])
    assert [] == tmp


def test_radix_sort4():
    tmp = radix_sort([1, 1, 1, 1, 1])
    assert [1, 1, 1, 1, 1] == tmp

def test_radix_sort5():
    for _ in range(10):
        a = random.sample(range(1, 100), 30)
        tmp = radix_sort(a)
        assert sorted(a) == tmp
