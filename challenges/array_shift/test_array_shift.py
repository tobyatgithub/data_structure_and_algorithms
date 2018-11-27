from .array_shift import insertShiftArray, removeShiftArray


def test_array_shift1():
    # case with even length input list
    assert(insertShiftArray([2,4,6,8],5) == [2,4,5,6,8])

def test_array_shift2():
    # case with odd length input list
    assert(insertShiftArray([4,8,15,23,42],16) == [4,8,15,16,23,42])

def test_array_shift3():
    # case with empty input list
    assert(insertShiftArray([],10) == [10])

def test_array_shift4():
    # case with input value to be a string
    assert(insertShiftArray([2,4,6,8],"5") == [2,4,"5",6,8])

def test_array_shift5():
    # case where we have a list with identical element
    assert(insertShiftArray([2,2,2,2],2) == [2,2,2,2,2])

def test_array_shift6():
    # case where we have empty input...hum...
    assert(insertShiftArray([2,2,2,2],None) == 'The input seems wrong, please input as insertShiftArray(a list, a number)')

def test_array_shift7():
    # case where we have a list with identical element
    assert(insertShiftArray([2,2,2,2],2.5) == [2,2,2.5,2,2])



def test_array_remove1():
    # case with even length input list
    assert(removeShiftArray([2,4,5,6,8]) == [2,4,6,8])

def test_array_remove2():
    # case with odd length input list
    assert(removeShiftArray([4,8,15,16,23,42]) == [4,8,15,23,42])

def test_array_remove3():
    # case with empty input list
    assert(removeShiftArray([]) == [])

def test_array_remove4():
    # case with input value to be a string
    assert(removeShiftArray([2,4,"5",6,8]) == [2,4,6,8])

def test_array_remove5():
    # case where we have a list with identical element
    assert(removeShiftArray([2,2,2,2]) == [2,2,2])

def test_array_remove6():
    # case where we have a list with identical element
    assert(removeShiftArray([3,3,4,5]) == [3,3,5])

def test_type_error1():
    # case for type error of input list
    assert(insertShiftArray({},2)=='The input seems wrong, please input as insertShiftArray(a list, a number)')


def test_type_error2():
    # case for type error of input list
    assert(removeShiftArray({})=='The input seems wrong, please input a list')
