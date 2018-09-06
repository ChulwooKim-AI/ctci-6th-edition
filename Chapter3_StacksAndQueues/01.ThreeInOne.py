"""Three in one

Describe how you could use a single array to implement three stacks.

Hints: 
#2
A stack is simply a data structure in which the most recently added elements are
removed first. Can you simulate a single stack using an array? Remember that there are
many possible solutions, and there are tradeoffs of each.
#12
We could simulate three stacks in an array by just allocating the first third of the array to
the first stack, the second third to the second stack, and the final third to the third stack.
One might actually be much bigger than the others, though. Can we be more flexible
with the divisions?
#38
If you want to allow for flexible divisions, you can shift stacks around. Can you ensure
that all available capacity is used?
#58
Try thinking about the array as circular, such that the end of the array "wraps around" to
the start of the array.
"""

import unittest

class StacksInArray:
    def __init__(self, k, size):
        self.top_of_stack = [None for _ in range(k)]
        self.stack_data = [None for _ in range(size)]
        self.next_index = [i+1 for i in range(size)]
        self.next_index[size-1] = None
        self.next_available = 0
    
    def push(self, stack, data):
        if stack < 0 or stack >= len(self.top_of_stack):
            raise IndexError("Out of index error")
        if self.next_available is None:
            raise Exception("All stacks are full.")
        
        current_index = self.next_available
        self.next_available = self.next_index[current_index]
        self.stack_data[current_index] = data
        self.next_index[current_index] = self.top_of_stack[stack]
        self.top_of_stack[stack] = current_index
    
    def pop(self, stack):
        if self.top_of_stack[stack] is None:
            raise Exception("This stack is empty.")
        
        current_index = self.top_of_stack[stack]
        value = self.stack_data[current_index]
        self.top_of_stack[stack] = self.next_index[current_index]
        self.next_index[current_index] = self.next_available
        self.next_available = current_index

        return value
    
    def show_stack_values(self, stack):
        current_index = self.top_of_stack[stack]
        result = ""
        while current_index:
            result += str(self.stack_data[current_index]) + " -> "
            current_index = self.next_index[current_index]
        result += "None"
        return result
    

class Test(unittest.TestCase):
    def setUp(self):
        self.stacks = StacksInArray(4, 10)
        self.stacks.push(0, 6)
        self.stacks.push(0, 7)
        self.stacks.push(1, 4)
        self.stacks.push(2, 1)
        self.stacks.push(0, 9)
        self.stacks.push(2, 5)
        self.stacks.push(1, 8)
    
    def test_pop(self):
        self.assertEqual(self.stacks.pop(0), 9)
        self.assertEqual(self.stacks.pop(2), 5)
    
    def test_push(self):
        self.stacks.push(1, 99)
        self.assertEqual(self.stacks.show_stack_values(1), "99 -> 8 -> 4 -> None")

    def test_full_exception(self):
        self.stacks.push(1, 5)
        self.stacks.push(1, 5)
        self.stacks.push(1, 5)
        self.assertRaises(Exception, self.stacks.push, 1, 5)
    
    def test_index_exception(self):
        self.assertRaises(IndexError, self.stacks.push, 9, 9)

if __name__ == "__main__":
    unittest.main()
