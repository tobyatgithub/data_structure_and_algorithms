from .array_binary_search import BinarySearch

def test_BinarySearch_exist():
    # check the function exists
    assert(BinarySearch)

def test_BinarySearch_inType():
    # check the output type setting
    assert(isinstance(BinarySearch([],2),int))

def test_BinarySearch_inType2():
    # check the input type alert
    assert(BinarySearch({},2) == -1)

def test_BinarySearch_simple1():
    # check a simple case, where value = the middle value of the input list
    assert(BinarySearch([1,2,3,4,5], 3) == 2)

def test_BinarySearch_simple2():
    # check empty list input
    assert(BinarySearch([], 3) == -1)

def test_BinarySearch_hard1():
    # check edge case1: value = the leftmost one of the input list
    assert(BinarySearch([1,2,3,4,5], 1) == 0)

def test_BinarySearch_hard2():
    # check edge case2: value = the rightmost one of the input list
    assert(BinarySearch([1,2,3,4,5], 5) == 4)

def test_BinarySearch_hard3():
    # check edge case2 but with an even length list
    assert(BinarySearch([1,2,4,5], 5) == 3)

def test_BinarySearch_hard4():
    # check non-exisiting case where the value is larger than everyone in input list
    assert(BinarySearch([1,2,3,4,5,60], 100) == -1)

def test_BinarySearch_hard5():
    # check non-exisiting case where the value is smaller than everyone in input list
    assert(BinarySearch([1,2,3,4,5,60], -10) == -1)

def test_BinarySearch_hard6():
    # check non-exisiting case where the value is somewhere in the middle
    assert(BinarySearch([1,5,20,40,50,60], 10) == -1)

def test_BinarySearch_hard7():
    # check non-exisiting case where the value is somewhere in the middle again
    assert(BinarySearch([1,2,3,4,5,60], 50) == -1)

def test_BinarySearch_hard8():
    # check exisiting case with a even length list and value is somewhere in the middle.
    assert(BinarySearch([1,5,20,40,50,60], 20) == 2)


