"""
In this file, we implement classic merge sort.
"""


def merge(list1, list2):
    """
    It takes in a sublist, break it in half, and
    merge it back in correct order.
    """
    out = []
    while list1 and list2:
        if list1[0] <= list2[0]:
            out.append(list1.pop(0))
        elif list1[0] > list2[0]:
            out.append(list2.pop(0))

    # if list1 runs out first
    if list2:
        out.extend(list2)
        del list2
    if list1:
        out.extend(list1)
        del list1

    return out


def merge_sort(in_list):
    """
    Merge sort takes in a list of numbers, divide this unsorted
    list into n sublists, each containing one element. Then repeatedly
    merge sublists to product new sorted sublists.

    In Merge_sort, we recursively break down inputs into sublist,
    and at the end we merge those sublist together recursively.
    Return sorted list.
    """
    if len(in_list) <= 1:
        return in_list

    mid = len(in_list)//2
    left = merge_sort(in_list[:mid])
    right = merge_sort(in_list[mid:])

    return merge(left, right)

