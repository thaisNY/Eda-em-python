class Node:
    
    def __init__ (self, data):
        self.data = data
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        """
            1. we need to implement the hash function: map a input to fixed size  O(1)
            2. insertion: we use hash function to find the block, insert on linked list O(1)
            3. removal: we use hash function to find the block, remove on linked list O(1)
            3. search: we use hash function to find the block, find an element in linked list O(1)
            
            collision: two hash key map to the same, m -> 1
        """
        self.hashmap = [None] * 1000
        
    def _hash(self, data):
        
        return hash(data) % 1000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        block = self._hash(key)
        if self.hashmap[block] is None:
            self.hashmap[block] = Node((key, value))
        else:
            current = self.hashmap[block]
            while current:
                k, v = current.data
                if k == key:
                    current.data = (key, value)
                    return
                if current.next is None:
                    break
                else:
                    current = current.next
            current.next = Node((key, value))
        
                
               
            
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        block = self._hash(key)
        if self.hashmap[block] is None:
            return -1
        current = self.hashmap[block]
        while current:
            k, v = current.data
            if k == key:
                return v
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        block = self._hash(key)
        if self.hashmap[block] is None:
            return
       
        current = self.hashmap[block]
        
        dummyNode = Node(0)
        dummyNode.next = current
        
        cur = dummyNode
        while cur and cur.next:
            k, v = cur.next.data
            if k == key:
                cur.next = cur.next.next
            cur = cur.next
        
        self.hashmap[block] = dummyNode.next
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)