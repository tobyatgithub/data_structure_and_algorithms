class HashTable:
    """
    A class for a hash table.
    """

    def __init__(self, size=8192):
        self.entries_count = 0
        self.alphabet_size = 52
        self.table_size = size
        self.hashtable = [[] for _ in range(size)]
        # usually we would like size to be a prime number
        #  to reduce chance of data collision

    def __repr__(self):
        return "<HashTable: {}>".format(self.hashtable)

    def __len__(self):
        count = 0
        for item in self.hashtable:
            count += len(item)
        return count

    def _hash_key(self, key):
        """
        takes in string key and turn that into a hash result
        """
        _key = ''.join(str(ord(c)) for c in key)
        return int(_key) % self.table_size

    def put(self, key, value):
        """
        Add a key and value into the hash table
        """
        if not isinstance(key, str):
            raise TypeError("Only strings can be used as keys")
        hash_ = self._hash_key(key)
        for i, item in enumerate(self.hashtable[hash_]):
            if item[0] == key:
                del self.hashtable[hash_][i]
                self.entries_count -= 1
        self.hashtable[hash_].append((key, value))
        self.entries_count += 1

    def get(self, key):
        """
        Retrieve a value from the hash table by key.
        """
        hash_ = self._hash_key(key)
        for i, item in enumerate(self.hashtable[hash_]):
            # why enumerate as we don't really use i?
            if item[0] == key:
                return item[1]
        # raise KeyError("Key not in hash table.")
        return False



