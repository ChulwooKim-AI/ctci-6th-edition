"""Sort stack

Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

Hints: 
#15
One way of sorting an array is to iterate through the array and insert each element into
a new array in sorted order. Can you do this with a stack?
#32
Imagine your secondary stack is sorted. Can you insert elements into it in sorted order?
You might need some extra storage. What could you use for extra storage?
#43
Keep the secondary stack in sorted order, with the biggest elements on the top. Use the
primary stack for additional storage.
"""

from Stack import Stack
import unittest

def sort_stack(stack):
    secondary_stack = Stack()    
    while not stack.is_empty():
        data = stack.pop()
        while not secondary_stack.is_empty() and secondary_stack.peek() < data:
            stack.push(secondary_stack.pop())                
        secondary_stack.push(data)        
    return secondary_stack.show()


class Test(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.stack.push(5)
        self.stack.push(3)
        self.stack.push(7)
        self.stack.push(9)
        self.stack.push(2)
    
    def test_sort_stack(self):
        self.assertEqual(sort_stack(self.stack), "2 - 3 - 5 - 7 - 9 - None")

if __name__ == "__main__":
    unittest.main()
