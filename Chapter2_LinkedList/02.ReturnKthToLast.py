"""Return Kth to last

Implement an algorithm to find the kth to last element of a singly linked list.
"""

from SingleLinkedList import SingleLinkedList
import unittest

def get_value_to_last(linkedlist, k):
    first_runner = linkedlist.head
    second_runner = linkedlist.head
    
    while second_runner is not None:
        if k != 0:
            second_runner = second_runner.next
            k -= 1
            continue
        first_runner = first_runner.next
        second_runner = second_runner.next
    
    return first_runner.data

class Test(unittest.TestCase):
    def test_get_value(self):
        sll = SingleLinkedList()
        sll.append(10)
        sll.append(9)
        sll.append(9)
        sll.append(5)
        sll.append(1)        
        self.assertEqual(get_value_to_last(sll, 3), 9)
        self.assertEqual(get_value_to_last(sll, 2), 5)

if __name__ == "__main__":
    unittest.main()
        
