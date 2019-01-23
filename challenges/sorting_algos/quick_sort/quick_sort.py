"""
In this file, we implement the classic quick sort with middle point
for pivot value.
"""


def quick_sort(in_list, _start, _end):
    """
    This quick_sort takes in a list as input, a _start int (usually 0) as the
    starting point from which we want to sort, and a _end int (usually =len(in_list))
    as the ending point from which we want to end sort.
    e.g. for a in_list [3,5,11,2,-1,10],
    if we want to sort the whole part: quick_sort(in_list, 0, 5)
    if we only want to sort the later half: quick_sort(in_list, 3, 5)
    """
    if _start < _end:
        pivot = partition(in_list, _start, _end)

        print("calling quick_sort on left with in_list = {}, start = {}, end = {}".format(in_list,_start,pivot))
        quick_sort(in_list, _start, pivot)
        print("calling quick_sort on right with in_list = {}, start = {}, end = {}".format(in_list,pivot+1,_end))
        quick_sort(in_list, pivot+1, _end)


def partition(in_list, _start, _end):
    """
    Take in a list, randomly select a pivot point, order the list such
    that all values smaller than the pivot point is on the left of pivot,
    and all values larger than the pivot point is on the right of pivot,
    and return a partition point
    """
    print("running partition with in_list = {}, start = {}, end = {}".format(in_list,_start, _end))
    mid_point = (_end + _start)//2
    # init swap, to avoid worst case.
    in_list[_start], in_list[mid_point] = in_list[mid_point], in_list[_start]
    pivot = in_list[_start]
    recent_closed_position = _start
    opened_positions = []
    print("in_list = {}, pivot = {}, and _strat now = {}".format(in_list, pivot, _start))

    for i in range(_start+1, _end):
        # we need to keep track of opened value
        tmp = in_list[i]
        opened_positions.append(i)
        print("\t i = {}, tmp={}, opened_pos = {}".format(i, tmp, opened_positions))
        if tmp < pivot:
            to_switch = opened_positions.pop(0)
            print("Switching now, to_switch = {}".format(to_switch))
            in_list[i], in_list[to_switch] = in_list[to_switch], in_list[i]
            recent_closed_position = to_switch

    # finish swap
    in_list[_start], in_list[recent_closed_position] = in_list[recent_closed_position], in_list[_start]
    print("returning p = {}, with in_list = {} \n".format(recent_closed_position, in_list))
    return recent_closed_position
