"""Remove Duplicates

Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from SingleLinkedList import SingleLinkedList 

def remove_duplicates(linked_list):
    temporary_buffer = {}
    current_node = linked_list.head
    previous_node = None
    while current_node is not None:
        if current_node.data in temporary_buffer:
            if previous_node is None:
                linked_list.head = current_node.next
            else:
                previous_node.next = current_node.next                
        else:
            temporary_buffer[current_node.data] = True
        previous_node = current_node
        current_node = current_node.next
    return linked_list

def remove_duplicates_without_buffer(linked_list):
    current_node = linked_list.head
    runner = current_node
    while current_node is not None:
        while runner.next is not None:
            if current_node.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current_node = current_node.next
        runner = current_node
    return linked_list

import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.sll = SingleLinkedList()
        self.sll.append(10)
        self.sll.append(9)
        self.sll.append(9)
        self.sll.append(5)
        self.sll.append(1)
        
    def test_append(self):                
        self.assertEqual(self.sll.values(), "10 -> 9 -> 9 -> 5 -> 1 -> None")    
    
    def test_remove(self):        
        self.sll.remove(5)
        self.assertEqual(self.sll.values(), "10 -> 9 -> 9 -> 1 -> None")    
    
    def test_remove_duplicates(self):
        remove_duplicates(self.sll)
        self.assertEqual(self.sll.values(), "10 -> 9 -> 5 -> 1 -> None")
    
    def test_remove_duplicates_without_buffer(self):        
        remove_duplicates_without_buffer(self.sll)
        self.assertEqual(self.sll.values(), "10 -> 9 -> 5 -> 1 -> None")

if __name__ == "__main__":
    unittest.main()
            