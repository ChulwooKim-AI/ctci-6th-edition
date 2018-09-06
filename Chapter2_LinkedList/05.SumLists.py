"""Sum Lists

You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7-) 1 -) 6) + (5 -) 9 -) 2) .Thatis,617 + 295.
Output: 2 -) 1 -) 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -) 1 -) 7) + (2 -) 9 -) 5).Thatis,617 + 295.
Output: 9 -) 1 -) 2. That is, 912.

Hints:
#7 
Of course, you could convert the linked lists to integers, compute the sum, and then
convert it back to a new linked list. If you did this in an interview, your interviewer would
likely accept the answer, and then see if you could do this without converting it to a
number and back.
#30 
Try recursion. Suppose you have two lists, A = 1 -> 5 -> 9 (representing 951) and B
2 -> 3 -> 6 -> 7 (representing 7632), and a function that operates on the remainder of the
lists (5 -> 9 and 3 -> 6 -> 7). Could you use this to create the sum method? What is the
relationship between sum(1->5->9, 2->3->6->7) and sum(5->9, 3->6->7)?
#71
Make sure you have considered linked lists that are not the same length.
#95
Does your algorithm work on linked lists like 9->7->8 and 6->8->5? Double check that.
#109
For the follow-up question: The issue is that when the linked lists aren't the same length,
the head of one linked list might represent the 1000's place while the other represents
the 1 D's place. What if you made them the same length? Is there a way to modify the
linked list to do that, without changing the value it represents?
"""

from SingleLinkedList import SingleLinkedList, Node
import unittest

def sum_lists(list1, list2):
    result = SingleLinkedList()
    list1_node = list1.head
    list2_node = list2.head
    carry = 0

    while list1_node and list2_node:
        sum = list1_node.data + list2_node.data + carry
        carry = sum // 10
        result.append(sum % 10)
        list1_node = list1_node.next
        list2_node = list2_node.next
    
    if list1_node is None and list2_node:
        while list2_node:
            sum = list2_node.data + carry
            result.append(sum % 10)
            list2_node = list2_node.next
    elif list2_node is None and list1_node:
        while list1_node:
            sum = list1_node.data + carry
            result.append(sum % 10)
            list1_node = list1_node.next
    elif list2_node is None and list1_node is None and carry:
        result.append(carry)

    return result

def sum_lists_by_converting(list1, list2):
    list1_node = list1.head
    list2_node = list2.head
    result = SingleLinkedList()

    converted_list1 = []
    converted_list2 = []
    while list1_node:
        converted_list1.insert(0, list1_node.data)
        list1_node = list1_node.next
    while list2_node:
        converted_list2.insert(0, list2_node.data)
        list2_node = list2_node.next
    
    sum = str(int(''.join(map(str, converted_list1))) + int(''.join(map(str, converted_list2))))

    for i in range(len(sum)-1, -1, -1):
        result.append(int(sum[i]))
    
    return result

def sum_lists_by_recursion(list1_node, list2_node, carry):
    result = Node(0)
    if list1_node is None and list2_node is None and carry == 0:
        return None
    sum = carry
    if list1_node:
        sum += list1_node.data
        list1_node = list1_node.next
    if list2_node:
        sum += list2_node.data
        list2_node = list2_node.next
    carry = sum // 10
    result.data = sum % 10
    result.next = sum_lists_by_recursion(list1_node, list2_node, carry)
    return result
    

class Test(unittest.TestCase):
    def setUp(self):
        self.sll_1 = SingleLinkedList()
        self.sll_1.append(7)
        self.sll_1.append(1)
        self.sll_1.append(6)
        self.sll_2 = SingleLinkedList()
        self.sll_2.append(5)
        self.sll_2.append(9)
        self.sll_2.append(2)
        self.sll_3 = SingleLinkedList()
        self.sll_3.append(9)
        self.sll_3.append(7)
        self.sll_3.append(8)
        self.sll_4 = SingleLinkedList()
        self.sll_4.append(6)
        self.sll_4.append(8)
        self.sll_4.append(5)
        
    def test_sum_lists(self):        
        self.assertEqual(sum_lists(self.sll_1, self.sll_2).values(), "2 -> 1 -> 9 -> None")
        self.assertEqual(sum_lists(self.sll_3, self.sll_4).values(), "5 -> 6 -> 4 -> 1 -> None")
    
    def test_sum_lists_by_converting(self):
        self.assertEqual(sum_lists_by_converting(self.sll_1, self.sll_2).values(), "2 -> 1 -> 9 -> None")
        self.assertEqual(sum_lists_by_converting(self.sll_3, self.sll_4).values(), "5 -> 6 -> 4 -> 1 -> None")

    def test_sum_lists_by_recursion(self):        
        result_list = SingleLinkedList()
        result_list.head = sum_lists_by_recursion(self.sll_1.head, self.sll_2.head, 0)
        self.assertEqual(result_list.values(), "2 -> 1 -> 9 -> None")
        result_list.head = sum_lists_by_recursion(self.sll_3.head, self.sll_4.head, 0)
        self.assertEqual(result_list.values(), "5 -> 6 -> 4 -> 1 -> None")

if __name__ == "__main__":
    unittest.main()