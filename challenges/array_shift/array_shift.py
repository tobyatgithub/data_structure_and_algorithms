def insertShiftArray(inArray, value):
    """
    This function takes in a list and the value to be added, and
    return a new list with the value added into the middle of the
    list.
    e.g. : insertShiftArray([2,4,6,8], 5) = [2,4,5,6,8]
           insertShiftArray([4,8,15,23,42],16) = [4,8,15,16,23,42]

    in: inArray - a list; value - a number (int or float)
    out: a new list
    """

    # 1. make sure the inArray is a list and value is a number
    try:
        # we raise type error if inArray is not a list, or the value is not a number
        if (type(inArray) is not list) or (not str(value).replace('.','',1).isdigit()):
            raise(TypeError)

        # find the location to insert
        index = (len(inArray) + 1)//2
        return inArray[:index] + [value] + inArray[index:]

    except TypeError:
        return("The input seems wrong, please input as insertShiftArray(a list, a number)")
    except KeyboardInterrupt:
        return("Program quit...")

def removeShiftArray(inArray):
    """
    This function takes a list and removes an element from the middle index and shifts other
    elements in the list to fill the new gap.
    e.g.: [2,3,4] => [2,4]
          [3,3,4,5] => [3,3,5]
    notice that for here we don't really mind the content type from the inArray.
    in: a list
    out: a new list
    """
    try:
        index = (len(inArray))//2
        return inArray[:index] + inArray[index+1:]
    except TypeError:
        return("The input seems wrong, please input a list")
    except KeyboardInterrupt:
        return("Program quit...")

### Notes:
# two ways of raising errors:
# 1. using pytest.raise:
#       in code, have the if condition as if bad condition: print(); raise()
#       in test, have the with pytest.raise(): balabala
# 2. use try-except to raise errors gracefully.
