"""
- Choose 100000 as the size of the list, which is 9 times larger than the `The number of operations`.
- Choose the basic hash function `index = key % list_size`, as there is no pre-knowledge of the input distribution and for convenience.
- Choose `-1` as the special marker when key/value is not available, since it is not a valid input key/value and we can directly return it if there is no matching records.
- Choose [Open Addressing](https://en.wikipedia.org/wiki/Hash_table#Open_addressing) as the collision resolution, as it is simple (save code to use another list or linked list).

Special notice, for `remove`, we CANNOT find the key/value pair and set it to the origin value [-1, -1]. It will make keys with the same *index* unreachable because of the gap when searching among collisions. So the trick here is to just `put` (update) its value to -1.
"""
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 100000
        self.store = [[-1, -1]] * self.size

        
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        pos = key % self.size
        while self.store[pos][0] != -1:
            if self.store[pos][0] == key:
                self.store[pos][1] = value
                return
            if pos == self.size:
                pos = -1
            pos += 1
        self.store[pos] = [key, value]

        
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        pos = key % self.size
        while self.store[pos][0] != -1:
            if self.store[pos][0] == key:
                return self.store[pos][1]
            if pos == self.size:
                pos = -1
            pos += 1
        return self.store[pos][1]
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.put(key, -1)
