"""Successor

Write an algorithm to find the "next" node (i .e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.

Hints: 
#79
Think about how an in-order traversal works and try to "reverse engineer" it.
#91
Here's one step of the logic: The successor of a specific node is the leftmost node of the
right subtree. What if there is no right subtree, though?
"""

import unittest

class Node:
    def __init__(self, data=None, parent=None):
        self.right = None
        self.left = None
        self.data = data
        self.parent = parent


class BinaryTreeWithParent:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self.__insert(self.root, data, None)
        
    def __insert(self, node, data, parent):
        if node is None:
            return Node(data, parent)
        if node.data < data:
            node.right = self.__insert(node.right, data, node)
        else:
            node.left = self.__insert(node.left, data, node)
        return node
    
    def get(self, data):
        return self.__get(self.root, data)
    
    def __get(self, node, data):
        if node is None:
            return None
        if node.data < data:
            return self.__get(node.right, data)
        elif node.data > data:
            return self.__get(node.left, data)
        else:
            return node
        

def inorder_successor(bst, node):
    if node.right:
        return leftmost(node.right)
    current_node = node
    parent_node = node.parent    
    while parent_node and parent_node.data < current_node.data:
        current_node = parent_node
        parent_node = parent_node.parent
    return parent_node

def leftmost(node):
    while node.left:
        node = node.left
    return node


class Test(unittest.TestCase):
    def setUp(self):
        self.bst = BinaryTreeWithParent()
        self.bst.insert(5)
        self.bst.insert(4)
        self.bst.insert(8)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(3)
        self.bst.insert(1)
        self.bst.insert(9)
    
    def test_inorder_successor(self):
        node = self.bst.get(2)
        self.assertEqual(inorder_successor(self.bst, node).data, 3)
        node = self.bst.get(8)
        self.assertEqual(inorder_successor(self.bst, node).data, 9)
        node = self.bst.get(9)
        self.assertEqual(inorder_successor(self.bst, node), None)
        
if __name__ == "__main__":
    unittest.main()