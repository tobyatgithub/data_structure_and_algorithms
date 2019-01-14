from .hash_table import HashTable


def test_import():
    assert HashTable


def test_hash_table1():
    tmp = HashTable()
    tmp.put(2)
    tmp.put(23)
    tmp.put(12)
    # import pdb; pdb.set_trace()
    assert 23 in tmp.table[23%11]
    assert 12 in tmp.table[12%11]
