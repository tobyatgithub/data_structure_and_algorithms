from ...data_structures.hash_table.hash_table import HashTable


def repeated_word(in_string):
    """
    Given a lengthy input string, without only the HashTable class,
    return the first word to occur more than once in that provided string.
    """
    storage = HashTable()
    if not isinstance(in_string, str):
        raise TypeError("please input in the type of string.")

    tmp_string = in_string.lower().replace(",","").replace(".","")
    for word in tmp_string.split():
        tmp_key = ''.join(str(ord(c)) for c in word)
        tmp_key = int(tmp_key) % storage.size
        if word in storage.table[tmp_key]:
            return(word)
        else:
            storage.table[tmp_key].append(word)

    print("No duplicates in this string!")
    return None
