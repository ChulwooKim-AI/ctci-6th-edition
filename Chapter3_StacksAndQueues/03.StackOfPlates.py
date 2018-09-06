"""Stack of plates

Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.

Hints: 
#64
You will need to keep track of the size of each substack. When one stack is full, you may
need to create a new stack.
#81
Popping an element at a specific substack will mean that some stacks aren't at full
capacity. Is this an issue? There's no right answer, but you should think about how to
handle this.
"""

from Stack import Stack
import unittest

class ExtendedStack(Stack):
    def get_size(self):
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next
            count += 1
        return count

class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def push(self, data):
        if len(self.stacks) == 0 or self.stacks[-1].get_size() == self.capacity:
            self.stacks.append(ExtendedStack())
        self.stacks[-1].push(data)
    
    def pop(self):
        if len(self.stacks) == 0:
            raise Exception("All stacks are empty")
        value = self.stacks[-1].peek()
        self.stacks[-1].pop()
        if self.stacks[-1].get_size() == 0:
            self.stacks.pop()
        return value
    
    def show(self):
        n = len(self.stacks)
        if n == 0:
            return "None"
        result = ""
        for i in range(n-1, -1, -1):
            current_node = self.stacks[i].head
            while current_node:                
                result += str(current_node.data) + " -> "
                current_node = current_node.next
        result += "None"
        return result

class Test(unittest.TestCase):
    def setUp(self):
        self.stack = SetOfStacks(3)        
    
    def test_push(self):
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(6)
        self.stack.push(1)
        self.assertEqual(self.stack.show(), "1 -> 6 -> 3 -> 2 -> None")
    
    def test_pop(self):
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(6)
        self.stack.pop()
        self.assertEqual(self.stack.show(), "3 -> 2 -> None")
        self.stack.push(1)
        self.stack.push(7)
        self.stack.pop()
        self.assertEqual(self.stack.show(), "1 -> 3 -> 2 -> None")

if __name__ == "__main__":
    unittest.main()