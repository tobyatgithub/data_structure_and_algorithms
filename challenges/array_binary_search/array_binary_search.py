
def BinarySearch(in_list, value):
    """
    input1: a sorted list (list)
    input2: a numeric value (int, float)
    out: a numeric value telling the position of the input2 in input1
        (will return -1 if input2 is not in input1.)

    Given a sorted list and a numeric value, use binary search method to find
    the location of the value in the list. Return -1 if value is not in list.
    We realize this binary method with the help of recurssion.

    Notice that, for wrong input, we will print a customized sentence,
    and return -1.
    """

    ### will it be good or bad? check first with if value in list ???
    # if value not in in_list:
    #     return -1
    # actually it would be bad...bcz to run int(xx) in list(xxx), you
    # need to iterate through the xxx no matter what.

    if not isinstance(in_list,list):
        print('Type error, the input list "%s" is not a list!' %in_list)
        return -1

    # check empty list
    if len(in_list) == 0:
        return -1

    # deal with boundary value, e.g. find 1 in [1,2,3]
    if len(in_list) == 1:
        if value == in_list[0]:
            return 0
        return -1

    mid_index = len(in_list)//2

    if value == in_list[mid_index]:
        return mid_index
    if value < in_list[mid_index]:
        return BinarySearch(in_list[:mid_index], value)
    if value > in_list[mid_index]:
        return BinarySearch(in_list[mid_index:], value) + \
        mid_index*(BinarySearch(in_list[mid_index:], value) != -1)
        # we need the multiple here, otherwise BinarySearch([1,2,3],100)
        # will give you 1-1 = 0 instead of -1. That is, the "+mid_index"
        # in the recurssive call will even out the -1 from the end case.

    # we shall never reach here...just in case
    assert("Error Opps! Value in list but didn't find?!")
    # return -1




