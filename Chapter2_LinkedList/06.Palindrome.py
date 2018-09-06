"""Palindrome

Implement a function to check if a linked list is a palindrome.

Hints:
#5
A palindrome is something which is the same when written forwards and backwards.
What if you reversed the linked list?
#13
Try using a stack.
#29
Assume you have the length of the linked list. Can you implement this recursively?
#61
In the recursive approach (we have the length of the list), the middle is the base case:
iSPermutation(middle) is true. The node x to the immediate left of the middle:
What can that node do to check if x- >middle- >y forms a palindrome? Now suppose
that checks out. What about the previous node a? If x- >middle- >y is a palindrome,
how can it check that a - >x - >middle - >y- >b is a palindrome?
#101
Go back to the previous hint. Remember: There are ways to return multiple values. You
can do this with a new class.   
"""

from SingleLinkedList import SingleLinkedList, Node
import unittest

def is_palindrome(linkedlist):
    first_runner = linkedlist.head
    second_runner = first_runner.next
    reverse_half = SingleLinkedList()

    while first_runner:        
        if second_runner.next is None:       
            temp_node = Node(first_runner.data)
            temp_node.next = reverse_half.head
            reverse_half.head = temp_node                    
        elif second_runner.next.next is None:            
            second_runner = second_runner.next        
        else:            
            second_runner = second_runner.next.next
        first_runner = first_runner.next
       
    current_node = linkedlist.head
    check_node = reverse_half.head
    while check_node:
        if check_node.data == current_node.data:
            check_node = check_node.next
            current_node = current_node.next
        else:
            return False
    return True

def is_palindrome_with_stack(linkedlist):    
    first_runner = linkedlist.head
    second_runner = first_runner.next
    stack = [first_runner.data]

    while second_runner.next:         
        if second_runner.next.next is None:
            second_runner = second_runner.next
            first_runner = first_runner.next
            break
        else:
            second_runner = second_runner.next.next       
        first_runner = first_runner.next
        stack.append(first_runner.data)
    
    first_runner = first_runner.next

    while first_runner:        
        if first_runner.data != stack.pop():
            return False
        first_runner = first_runner.next

    return True

def is_palindrome_recursively(linkedlist):
    first_runner = linkedlist.head
    second_runner = linkedlist.head

    while second_runner.next and second_runner.next.next:
        first_runner = first_runner.next
        second_runner = second_runner.next.next
    
    _, result = check_palindrome(linkedlist.head, first_runner)

    return result

def check_palindrome(node1, node2):
    if node2.next is None:
        return (node1, True)
    node2 = node2.next
    node1, _ = check_palindrome(node1, node2)
    if node1 and node1.data == node2.data:
        return (node1.next, True)
    else:
        return (None, False)

class Test(unittest.TestCase):
    def setUp(self):
        self.sll_1 = SingleLinkedList()
        self.sll_1.append(7)
        self.sll_1.append(1)
        self.sll_1.append(6)
        self.sll_1.append(1)
        self.sll_1.append(7)
        self.sll_2 = SingleLinkedList()
        self.sll_2.append(7)
        self.sll_2.append(1)
        self.sll_2.append(6)
        self.sll_2.append(6)
        self.sll_2.append(1)
        self.sll_2.append(7)
        self.sll_3 = SingleLinkedList()
        self.sll_3.append(7)
        self.sll_3.append(1)
        self.sll_3.append(5)
        self.sll_3.append(6)
        self.sll_3.append(1)
        self.sll_3.append(7)

    def test_is_palindrome(self):        
        self.assertTrue(is_palindrome(self.sll_1))
        self.assertTrue(is_palindrome(self.sll_2))
        self.assertFalse(is_palindrome(self.sll_3))
    
    def test_is_palindrome_with_stack(self):        
        self.assertTrue(is_palindrome_with_stack(self.sll_1))
        self.assertTrue(is_palindrome_with_stack(self.sll_2))
        self.assertFalse(is_palindrome_with_stack(self.sll_3))
    
    def test_is_palindrome_recursively(self):        
        self.assertTrue(is_palindrome_recursively(self.sll_1))
        self.assertTrue(is_palindrome_recursively(self.sll_2))
        self.assertFalse(is_palindrome_recursively(self.sll_3))

if __name__ == "__main__":
    unittest.main()