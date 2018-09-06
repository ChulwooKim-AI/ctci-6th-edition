"""Loop Detection
Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.

EXAMPLE
Input: A -> B -> C -> D -> E -> C [thesameCasearlier]
Output: C

Hints: 
#50 
There are really two parts to this problem. First, detect if the linked list has a loop.
Second, figure out where the loop starts.
#69
To identify if there's a cycle, try the "runner" approach described on page 93. Have one
pointer move faster than the other.
#83
You can use two pointers, one moving twice as fast as the other. If there is a cycle, the
two pointers will collide. They will land at the same location at the same time. Where do
they land? Why there?
#90
If you haven't identified the pattern of where the two pointers start, try this: Use the
linked list 1->2->3->4->5->6->7->8->9->?, where the? links to another node. Try
making the? the first node (that is, the 9 points to the 1 such that the entire linked list
is a loop). Then make the? the node 2. Then the node 3. Then the node 4. What is the
pattern? Can you explain why this happens?
"""

from SingleLinkedList import SingleLinkedList
import unittest

def find_starting_point(linkedlist):
    first_runner = linkedlist.head
    second_runner = linkedlist.head

    while second_runner:
        first_runner = first_runner.next
        second_runner = second_runner.next.next
        if first_runner is second_runner:
            break
    if second_runner is None and second_runner.next is None:
        return None
    
    second_runner = linkedlist.head
    while first_runner:
        if first_runner is second_runner:
            return first_runner.data
        first_runner = first_runner.next
        second_runner = second_runner.next
    return None


class CircularLinkedList(SingleLinkedList):
    def make_circuit(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = self.head


class SingleLinkedListWithNode(SingleLinkedList):
    def append_node(self, node):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node


class Test(unittest.TestCase):
    def setUp(self):
        cll = CircularLinkedList()
        cll.append(2)
        cll.append(5)
        cll.append(7)
        cll.append(9)
        cll.append(1)
        cll.make_circuit()
        self.sll = SingleLinkedListWithNode()
        self.sll.append(4)
        self.sll.append(5)
        self.sll.append(6)
        self.sll.append_node(cll.head)
    
    def test_find_starting_point(self):
        self.assertEqual(find_starting_point(self.sll), 2)

if __name__ == "__main__":
    unittest.main()
