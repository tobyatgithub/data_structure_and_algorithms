"""
In this file we implement the selection sort. Its complexity
is O(n^2) for time and O(n) for space.

Reference: GeekforGeek
The selection sort algorithm sorts an array by repeatedly
finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning. The
algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element
(considering ascending order) from the unsorted subarray
is picked and moved to the sorted subarray.
"""


def selection_sort(in_list):
    """
    Given a list, return a sorted list. Inplace not required.
    """
    # check input
    if not isinstance(in_list, list):
        raise TypeError("Please input a list for selection sort.")

    tmp_list = in_list.copy()
    output = []
    for _ in range(len(tmp_list)):
        output.append(min(tmp_list))
        tmp_list.remove(min(tmp_list))

    return output


