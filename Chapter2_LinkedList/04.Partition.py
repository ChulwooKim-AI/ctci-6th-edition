"""Partition

Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from SingleLinkedList import SingleLinkedList
import unittest

def partition_by_value(linkedlist, partition):
    left_list = SingleLinkedList()
    right_list = SingleLinkedList()
    current_node = linkedlist.head

    while current_node is not None:
        if current_node.data < partition:
            left_list.append(current_node.data)            
        else:
            right_list.append(current_node.data)
        current_node = current_node.next
    
    left_node = left_list.head
    while left_node.next is not None:              
        left_node = left_node.next
    left_node.next = right_list.head
    linkedlist.head = left_list.head

def partition_in_place(linkedlist, partition):
    previous_node = None
    current_node = linkedlist.head

    while current_node:
        if previous_node and current_node.data < partition:
            previous_node.next = current_node.next
            current_node.next = linkedlist.head
            linkedlist.head = current_node
            current_node = previous_node.next
        else:
            previous_node = current_node
            current_node = current_node.next

class Test(unittest.TestCase):
    def setUp(self):
        self.sll = SingleLinkedList()
        self.sll.append(10)
        self.sll.append(1)
        self.sll.append(9)
        self.sll.append(5)
        self.sll.append(2)
    def test_partition(self):                
        partition_by_value(self.sll, 5)
        self.assertEqual(self.sll.values(), "1 -> 2 -> 10 -> 9 -> 5 -> None")

    def test_partition_in_place(self):            
        partition_in_place(self.sll, 5)
        self.assertEqual(self.sll.values(), "2 -> 1 -> 10 -> 9 -> 5 -> None")

if __name__ == "__main__":
    unittest.main()