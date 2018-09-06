"""Delete Middle Node

Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node, not necessarily the exact middle) 
of a singly linked list, given only access to that node.

EXAMPLE
Input: the node c from the linked list a -> b -> c -> d -> e -> f
Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
"""

from SingleLinkedList import SingleLinkedList
import unittest

def delete_middle_node(linkedlist):
    first_runner = linkedlist.head
    second_runner = first_runner.next
    previous_node = None

    while second_runner is not None:                
        if second_runner.next is None:
            previous_node.next = first_runner.next
            second_runner = second_runner.next
        elif second_runner.next.next is None:
            first_runner.next = first_runner.next.next
            second_runner = second_runner.next.next
        else:
            second_runner = second_runner.next.next
        previous_node = first_runner
        first_runner = first_runner.next
    
class Test(unittest.TestCase):
    def test_delete_middle_node(self):
        sll = SingleLinkedList()
        sll.append(10)
        sll.append(9)
        sll.append(9)
        sll.append(5)
        sll.append(1)        
        delete_middle_node(sll)
        self.assertEqual(sll.values(), "10 -> 9 -> 5 -> 1 -> None")
        delete_middle_node(sll)
        self.assertEqual(sll.values(), "10 -> 5 -> 1 -> None")

if __name__ == "__main__":
    unittest.main()