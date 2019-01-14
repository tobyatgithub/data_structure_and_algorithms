class HashTable:
    def __init__(self, size=11):
        self.size = size  # number of buckets
        self.table = {}
        # usually we would like size to be a prime number
        #  to reduce chance of data collision

    def put(self, data):
        """
        Given a hash table class, and a data point to
        put into this hash table. This function will
        generate the key for this data according to
        self.size and store that data into it.
        Data collision is solved by a list.
        """
        key = data % self.size
        self.table.setdefault(key,[])
        self.table[key].append(data)
        return self
