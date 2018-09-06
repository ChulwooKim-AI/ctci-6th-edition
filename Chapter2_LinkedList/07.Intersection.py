"""Intersection

Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

Hints:
#20
You can do this in O(A+B) time and O(1) additional space. That is, you do not need a
hash table (although you could do it with one).
#45
Examples will help you. Draw a picture of intersecting linked lists and two equivalent
linked lists (by value) that do not intersect.
#55 
Focus first on just identifying if there's an intersection.
#65
Observe that two intersecting linked lists will always have the same last node. Once they
intersect, all the nodes after that will be equal.
#76
You can determine if two linked lists intersect by traversing to the end of each and
comparing their tails.
#93
Now, you need to find where the linked lists intersect. Suppose the linked lists were the
same length. How could you do this?
#111
If the two linked lists were the same length, you could traverse forward in each until you
found an element in common. Now, how do you adjust this for lists of different lengths?
#120
Try using the difference between the lengths of the two linked lists.
#129
If you move a pointer in the longer linked list forward by the difference in lengths, you
can then apply a similar approach to the scenario when the linked lists are equal.

"""

from SingleLinkedList import SingleLinkedList, Node
import unittest

def intersect_by_hashtable(list1, list2):    
    nodes = {}
    list1_node = list1.head
    list2_node = list2.head

    while list1_node:
        nodes[list1_node] = True
        list1_node = list1_node.next
    
    while list2_node:
        if list2_node in nodes:
            return list2_node
        list2_node = list2_node.next
    return None

def get_length(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length

def move_as_difference(node, difference):
    for _ in range(difference):
        node = node.next    
    return node

def intersect_in_place(list1, list2):
    list1_node = list1.head
    list2_node = list2.head

    length_of_list1 = get_length(list1_node)
    length_of_list2 = get_length(list2_node)

    if length_of_list1 > length_of_list2:
        list1_node = move_as_difference(list1_node, length_of_list1-length_of_list2)
    elif length_of_list1 < length_of_list2:
        list2_node = move_as_difference(list2_node, length_of_list2-length_of_list1)
    
    while list1_node:
        if list1_node is list2_node:
            return list1_node
        list1_node = list1_node.next
        list2_node = list2_node.next

    return None

def node_values(node):
    result = ""    
    while node:
        result += str(node.data) + " -> "
        node = node.next
    return result + "None"


class SingleLinkedListWithNode(SingleLinkedList):
    def append_node(self, node):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
    
    
class Test(unittest.TestCase):
    def setUp(self):
        node = Node(3, Node(6, Node(9)))        
        self.sll_1 = SingleLinkedListWithNode()
        self.sll_1.append(7)
        self.sll_1.append(1)
        self.sll_1.append(6)
        self.sll_1.append(1)
        self.sll_1.append(7)
        self.sll_1.append_node(node)
        self.sll_2 = SingleLinkedListWithNode()        
        self.sll_2.append(4)
        self.sll_2.append(5)
        self.sll_2.append_node(node)

    def test_intersect_in_place(self):        
        self.assertEqual(node_values(intersect_in_place(self.sll_1, self.sll_2)), "3 -> 6 -> 9 -> None")
    
    def test_intersect_by_hashtable(self):        
        self.assertEqual(node_values(intersect_by_hashtable(self.sll_1, self.sll_2)), "3 -> 6 -> 9 -> None")

if __name__ == "__main__":
    unittest.main()
        