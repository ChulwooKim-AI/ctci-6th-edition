"""Queue via stacks

Implement a MyQueue class which implements a queue using two stacks.

Hints: 
#98
The major difference between a queue and a stack is the order of elements. A queue
removes the oldest item and a stack removes the newest item. How could you remove
the oldest item from a stack if you only had access to the newest item?
#114
We can remove the oldest item from a stack by repeatedly removing the newest item
(inserting those into the temporary stack) until we get down to one element. Then, after
we've retrieved the newest item, putting all the elements back. The issue with this is
that doing several pops in a row will require 0 (N) work each time. Can we optimize for
scenarios where we might do several pops in a row?
"""

from Stack import Stack
import unittest

class MyQueue:
    def __init__(self):
        self.enqueue = Stack()
        self.dequeue = Stack()
    
    def push(self, data):
        self.enqueue.push(data)
    
    def pop(self):
        while self.enqueue.peek():
            self.dequeue.push(self.enqueue.pop())
        self.dequeue.pop()
        while self.dequeue.peek():
            self.enqueue.push(self.dequeue.pop())
    
    def show(self):
        result = ""
        current_node = self.enqueue.head
        while current_node:
            result += str(current_node.data) + " -> "
            current_node = current_node.next
        result += "None"
        return result


class Test(unittest.TestCase):
    def setUp(self):
        self.queue = MyQueue()
        self.queue.push(5)
        self.queue.push(2)
    
    def test_push(self):
        self.queue.push(6)
        self.queue.push(7)
        self.assertEqual(self.queue.show(), "7 -> 6 -> 2 -> 5 -> None")
    
    def test_pop(self):
        self.queue.push(1)
        self.queue.push(3)
        self.queue.pop()
        self.assertEqual(self.queue.show(), "3 -> 1 -> 2 -> None")
        self.queue.pop()
        self.assertEqual(self.queue.show(), "3 -> 1 -> None")

if __name__ == "__main__":
    unittest.main()