class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self, item):
        new_item = Node(item)
        if self.tail:
            self.tail.next = new_item
        self.tail = new_item
        if self.head is None:
            self.head = self.tail
    
    def remove(self):
        if self.head is None:
            return None
        result = self.head.data
        self.head = self.head.next
        return result
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.data
    
    def isEmpty(self):
        return self.head is None

    def show(self):
        result = ""
        current_node = self.head
        while current_node:
            result += str(self.head.data) + " - "
            current_node = current_node.next
        result += "None"
        return result