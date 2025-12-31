class HashTable:

    def __init__(self, table_size): # add appropriate attributes, NO default size
        ''' Initializes an empty hash table with a size that is the smallest
            prime number that is >= table_size (i.e. if 10 is passed, 11 will 
            be used, if 11 is passed, 11 will be used.)'''
        self.table_size = self.next_prime(table_size)
        self.hashtable = [None] * self.table_size
        self.num_items = 0

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value can be anything (Object, None, list, etc.).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased
        to the next prime greater than 2*table_size.'''
        self.key = key
        self.value = value
        index = self.horner_hash_func(self.key) % self.table_size

        i = 0
        while i < self.table_size:
            findex = (index + i**2) % self.table_size
            # print(f"insert Debug: key={key}, value={value}, index={index}, i={i}, findex={findex}, type(findex)={type(findex)}")
            if self.hashtable[findex] == None:
                self.hashtable[findex] = (self.key, self.value)
                self.num_items += 1
                break
            elif self.hashtable[findex][0] == self.key:
                self.hashtable[findex] = (self.key, self.value)
                break
            i += 1

        load = self.num_items / self.table_size
        if load > 0.5:
            self.table_size = self.next_prime(self.table_size * 2)
            old_table = self.hashtable
            self.hashtable = [None] * self.table_size
            self.num_items = 0
            for entry in old_table:
                if entry != None:
                    self.insert(entry[0], entry[1])


    def horner_hash_func(self, key:str):
        ''' Compute the hash value by using Horner’s rule, as described in project specification.
            This method ***should not*** mod with the table size'''
        # keylist = list(key)
        # key = 0
        # n = min(8, len(keylist))
        # for i in range(n):
        #     key += (ord(keylist[i]) * 31**(n-1-i))
        # return key
        hash_value = 0
        for char in key[:8]:
            hash_value = hash_value * 31 + ord(char)
        return hash_value
        
    def next_prime(self, n):
        ''' Find the next prime number that is > n.'''
        # print(f"next_prime Debug: Input n={n}, type(n)={type(n)}")
        n = int(n)
        if n <= 1:
            return 2
        if n ==2 or n == 3:
            return n
        if n % 2 == 0 or n % 3 == 0:
            return self.next_prime(n + 1)
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return self.next_prime(n + 1)
            i += 6
        return n

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        self.key = key
        index = self.horner_hash_func(self.key) % self.table_size
        i = 0
        findex = index
        while i < self.table_size:
            if self.hashtable[findex] is None:
                return False
            elif self.hashtable[findex][0] == self.key:
                return True
            else:
                i += 1
                findex = (index + (i ** 2)) % self.table_size

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        self.key = key
        index = self.horner_hash_func(self.key) % self.table_size
        i = 0
        while i < self.table_size:
            findex = (index + i ** 2) % self.table_size
            if self.hashtable[findex] == None:
                return None
            elif self.hashtable[findex][0] == self.key:
                return findex
            i += 1

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        keys = []
        for entry in self.hashtable:
            if entry != None:
                keys.append(entry[0])
        return keys


    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        self.key = key
        index = self.horner_hash_func(self.key) % self.table_size
        i = 0
        while i < self.table_size:
            findex = (index + i ** 2) % self.table_size
            if self.hashtable[findex] == None:
                return None
            elif self.hashtable[findex][0] == self.key:
                return self.hashtable[findex][1]
            i += 1

    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.num_items/self.table_size
