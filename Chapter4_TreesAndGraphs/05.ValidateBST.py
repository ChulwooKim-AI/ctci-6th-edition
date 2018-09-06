"""Validate BST

Implement a function to check if a binary tree is a binary search tree.

Hints: 
#35
If you traversed the tree using an in-order traversal and the elements were truly in
the right order, does this indicate that the tree is actually in order? What happens for
duplicate elements? If duplicate elements are allowed, they must be on a specific side
(usually the left).
#57
To be a binary search tree, it's not sufficient that the left. value <= current.
value < right. value for each node. Every node on the left must be less than the
current node, which must be less than all the nodes on the right.
#86
If every node on the left must be less than or equal to the current node, then this is really
the same thing as saying that the biggest node on the left must be less than or equal to
the current node.
#113
Rather than validating the current node's value against leftTree. max and
rightTree. min, can we flip around the logic? Validate the left tree's nodes to ensure
that they are smaller than current. value.
#128
Think about the checkBST function as a recursive function that ensures each node is
within an allowable (min, max) range. At first, this range is infinite. When we traverse
to the left, the min is negative infinity and the max is root. value. Can you implement
this recursive function and properly adjust these ranges as you traverse the tree?
"""
from BinaryTree import BinaryTree, Node
import math
import unittest

#Time complexity : O(n)
def validate_bst(bst):
    return __validate_bst(bst.root, -math.inf, math.inf)

def __validate_bst(node, minvalue, maxvalue):
    if node is None:
        return True
    if node.data < minvalue or node.data > maxvalue:
        return False
    return __validate_bst(node.left, minvalue, node.data - 1) \
        and __validate_bst(node.right, node.data+1, maxvalue)

#Time complexity : O(n)
def validate_bst_in_order(bst):
    previous_node = None
    return __validate_bst_in_order(bst.root, previous_node)

def __validate_bst_in_order(node, previous_node):    
    if node:
        if not __validate_bst_in_order(node.left, previous_node):
            return False
        if previous_node and previous_node > node.data:
            return False        
        previous_node = node.data
        if not __validate_bst_in_order(node.right, previous_node):
            return False
    return True
        

class Test(unittest.TestCase):
    def setUp(self):
        self.bst = BinaryTree()
        self.bst.insert(5)
        self.bst.insert(4)
        self.bst.insert(8)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(1)
        self.bst.insert(9)
    
    def test_validate_bst(self):
        self.assertTrue(validate_bst(self.bst))
    
    def test_validate_bst_in_order(self):
        self.assertTrue(validate_bst_in_order(self.bst))

if __name__ == "__main__":
    unittest.main()