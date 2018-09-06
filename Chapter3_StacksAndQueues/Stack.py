class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, head=None):
        self.head = head

    def push(self, item):
        new_item = Node(item)
        new_item.next = self.head
        self.head = new_item
    
    def pop(self):
        if self.head is None:
            return None
        result = self.head.data
        self.head = self.head.next
        return result
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.data
    
    def is_empty(self):
        return self.head is None
        
    def show(self):
        result = ""
        current_node = self.head
        while current_node:
            result += str(current_node.data) + " - "
            current_node = current_node.next
        result += "None"
        return result