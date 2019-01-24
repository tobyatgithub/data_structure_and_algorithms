"""
In this file, we implement radix sort. Radix sort is different from other sorting
algorithms. Radix sort is a non-comparative integer sorting algorithm that sorts
data with integer keys by grouping keys by the individual digits which share the
same significant position and value.
"""

def radix_sort(in_list, b=10):
    """
    this fucntion takes in an in_list contains numbers, sort the numbers
    in it according to the digit defined by b. b is set to be 10 as default,
    which will mean given [12, 42, 33], we will first sort the first digit
    (2, 2, 3), and then the second digit (1, 4, 3) -> (1, 3, 4). Notice that
    if we have tiers, we keep the original sequence.
    Input: in_list a list with numbers, b a number indicates digit.
    Output: a sorted list.
    """
    # first we find the max number of time we need to iterate through
    longest = 0
    for i in in_list:
        if len(str(i)) > longest:
            longest = len(str(i))

    # second, we know that at each digit, we at most can get b different
    # values
    for j in range(1, longest+1):
        tmp = [[] for _ in range(b)]
        for ele in in_list:
            try:
                digit = int(str(ele)[-j])
            except:
                digit = 0
            tmp[digit].append(ele)
        in_list = sum(tmp, [])

    return in_list


