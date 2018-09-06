"""Stack Min

How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

Hints: 
#27
Observe that the minimum element doesn't change very often. It only changes when a
smaller element is added, or when the smallest element is popped.
#59
What if we kept track of extra data at each stack node? What sort of data might make it
easier to solve the problem?
#78
Consider having each node know the minimum of its "substack" (all the elements
beneath it, including itself).
"""

import unittest

class Node:
    def __init__(self, data=None, min=None, next=None):
        self.data = data
        self.next = next
        self.min = min

class StackMin:
    def __init__(self, head=None):
        self.head = head
    
    def push(self, data):        
        new_node = Node(data)        
        if self.head is None or self.head.min > data:            
            new_node.min = data
        else:
            new_node.min = self.head.min
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):        
        if self.head is None:
            return None            
        value = self.head.data        
        self.head = self.head.next
            
        return value
    
    def get_min(self):
        return self.head.min


from Stack import Stack

class StackMinWithSubStack:
    min_stack = Stack()
    data_stack = Stack()

    def push(self, data):
        if self.min_stack.is_empty() or self.min_stack.peek() > data:            
            self.min_stack.push(data)
        self.data_stack.push(data)
    
    def pop(self):
        if self.data_stack.is_empty():
            raise Exception("Stack is empty")
        if self.data_stack.peek() == self.min_stack.peek():
            self.min_stack.pop()
        self.data_stack.pop()
    
    def get_min(self):
        return self.min_stack.peek()
    
    def peek(self):
        return self.data_stack.peek()
    

class Test(unittest.TestCase):
    def setUp(self):
        self.stack = StackMin()
        self.stack.push(5)
        self.stack.push(6)
        self.stack.push(8)
        self.substack = StackMinWithSubStack()
        self.substack.push(5)
        self.substack.push(6)
        self.substack.push(8)

    def test_min(self):
        self.assertEqual(self.stack.get_min(), 5)
        self.stack.push(2)
        self.assertEqual(self.stack.get_min(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.get_min(), 5)
    
    def test_min_with_substack(self):
        self.assertEqual(self.substack.get_min(), 5)
        self.substack.push(2)
        self.assertEqual(self.substack.get_min(), 2)
        self.substack.pop()
        self.assertEqual(self.substack.get_min(), 5)

if __name__ == "__main__":
    unittest.main()