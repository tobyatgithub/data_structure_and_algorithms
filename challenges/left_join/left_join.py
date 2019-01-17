"""
In this file, we write a function that performs left join on
two hash table inputs.
"""


def left_join(hash1, hash2, method='left'):
    if method == 'right':
        hash1, hash2 = hash2, hash1
    out = []
    for buckets in hash1.hashtable:
        for items in buckets:
            key = items[0]
            left_value = items[1]
            right_value = hash2.get(key)
            if right_value:
                out.append([key, left_value, right_value])
            else:
                out.append([key, left_value, "None"])
    return out
