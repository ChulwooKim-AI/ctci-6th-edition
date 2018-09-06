"""First Common Ancestor

Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.

Hints: 
#10
If each node has a link to its parent, we could leverage the approach from question 2.7
on page 95. However, our interviewer might not let us make this assumption.
#16
The first common ancestor is the deepest node such that p and q are both descendants.
Think about how you might identify this node.
#28
How would you figure out if p is a descendent of a node n?
#36
Start with the root. Can you identify if root is the first common ancestor? If it is not, can
you identify which side of root the first common ancestor is on?
#46
Try a recursive approach. Check if p and q are descendants of the left subtree and the
right subtree. If they are descendants of different subtrees, then the current node is the
first common ancestor. If they are descendants of the same subtree, then that subtree
holds the first common ancestor. Now, how do you implement this efficiently?
#70 
In the more naive algorithm, we had one method that indicated if x is a descendent
of n, and another method that would recurse to find the first common ancestor. This is
repeatedly searching the same elements in a subtree. We should merge this into one
firstCommonAncestor function. What return values would give us the information
we need?
#80
The firstCommonAncestor function could return the first common ancestor (if p
and q are both contained in the tree), p if P is in the tree and not q, q if q is in the tree
and not p, and null otherwise.
#96
Careful! Does your algorithm handle the case where only one node exists? What will
happen? You might need to tweak the return values a bit.
"""

import unittest

class Node:
    def __init__(self, data=None, parent=None):
        self.right = None
        self.left = None
        self.data = data
        self.parent = parent

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def put(self, data):
        if self.root:
            self.__put(self.root, data)
        else:
            self.root = Node(data)
    
    def __put(self, node, data):
        if node.data < data:
            if node.right:
                self.__put(node.right, data)
            else:
                node.right = Node(data, node)
        else:
            if node.left:                
                self.__put(node.left, data)
            else:
                node.left = Node(data, node)

def find_common_ancestor(tree, node1, node2):
    if tree.root is None:
        return None
    result = __find_common_ancestor(tree.root, node1, node2)    
    return None if result is None else result.data

def __find_common_ancestor(current_node, node1, node2):
    if current_node.data == node1 or current_node.data == node2:        
        return current_node.parent
    check_node = check_subtree(current_node, node1)    
    if check_node == check_subtree(current_node, node2):
        if check_node == "right":
            return __find_common_ancestor(current_node.right, node1, node2)
        else:
            return __find_common_ancestor(current_node.left, node1, node2)
    else:        
        return current_node

def check_subtree(current_node, check_node):
    if current_node is None:
        return None
    if current_node.left and __check_subtree(current_node.left, check_node):
        return "left"
    elif current_node.right and __check_subtree(current_node.right, check_node):
        return "right"

def __check_subtree(current_node, check_node):
    if current_node is None:
        return False
    if current_node.data == check_node:
        return True
    return __check_subtree(current_node.left, check_node) or __check_subtree(current_node.right, check_node)


class Test(unittest.TestCase):
    def setUp(self):
        self.bst = BinaryTree()
        self.bst.put(5)
        self.bst.put(4)
        self.bst.put(8)
        self.bst.put(2)
        self.bst.put(7)
        self.bst.put(9)
        self.bst.put(1)
        self.bst.put(3)
    
    def test_first_common_ancestor(self):
        self.assertEqual(find_common_ancestor(self.bst, 1, 3), 2)        
        self.assertEqual(find_common_ancestor(self.bst, 2, 9), 5)
        self.assertEqual(find_common_ancestor(self.bst, 2, 4), 5)
        self.assertEqual(find_common_ancestor(self.bst, 2, 5), None)

if __name__ == "__main__":
    unittest.main()
