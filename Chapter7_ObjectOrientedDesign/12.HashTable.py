"""Hash Table

Design and implement a hash table which uses chaining (linked lists) to handle collisions.

Hints: 
#287
In order to handle collisions, the hash table should be an array of linked lists.
#307
Think carefully about what information the linked list node needs to contain.
"""

class LinkedListNode:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
    
    def put(self, key, value):
        node = self.get_node_for_key(key)
        if node:
            node.value = value
        else:
            node = LinkedListNode(key, value)
            index = self.get_index_for_key(key)
            if self.slots[index]:
                node.next = self.slots[index]
                node.next.prev = node
            else:
                self.slots[index] = node
        
    def get_index_for_key(self, key):
        return key % self.size
    
    def get_node_for_key(self, key):
        current_node = self.slots[self.get_index_for_key(key)]
        while current_node:
            if current_node.key == key:
                return current_node
            current_node = current_node.next
        return None
    
    def get(self, key):
        if key is None:
            return None
        node = self.get_node_for_key(key)
        return node.value if node else None
    
    def remove(self, key):
        node = self.get_node_for_key(key)
        if node is None:
            return None
        if node.prev:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        else:
            self.slots[self.get_index_for_key(key)] = node.next
        return node.value


if __name__ == "__main__":
    hashtable = HashTable()
    hashtable.put(123, "one_two_three")
    hashtable.put(675, "six_seven_five")
    hashtable.put(23, "two_three")
    hashtable.put(82, "eight_two")
    print(hashtable.get(82))
    hashtable.remove(82)
    print(hashtable.get(82))