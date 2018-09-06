"""Minimal Tree 

Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.

Hints: 
#19
A minimal binary tree has about the same number of nodes on the left of each node as
on the right. Let's focus on just the root for now. How would you ensure that about the
same number of nodes are on the left of the root as on the right?
#73
You could implement this by finding the "ideal" next element to add and repeatedly
calling insertValue. This will be a bit inefficient, as you would have to repeatedly
traverse the tree. Try recursion instead. Can you divide this problem into subproblems?
#176
Think about what sort of expectations on freshness and accuracy of data is expected.
Does the data always need to be 100% up to date? Is the accuracy of some products
more important than others?
"""

import unittest

class Node:
    def __init__(self, data=None):
        self.right = None
        self.left = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            self.__insert(self.root, data)
        else:
            self.root = Node(data)
    
    def __insert(self, node, data):
        if node.data < data:
            if node.right:
                self.__insert(node.right, data)
            else:
                node.right = Node(data)            
        else:
            if node.left:
                self.__insert(node.left, data)
            else:
                node.left = Node(data)
    
    def show(self):
        if self.root is None:
            return None
        return self.__pre_order(self.root, path=[])
    
    def __pre_order(self, node, path):
        if node:            
            path.append(node.data)
            self.__pre_order(node.left, path)            
            self.__pre_order(node.right, path)
            return path


class MinimalTree(BinarySearchTree):
    def make_tree(self, sorted_array):
        self.root = self.__make_tree(sorted_array, 0, len(sorted_array)-1)
    
    def __make_tree(self, list, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = Node(list[mid])
        node.left = self.__make_tree(list, start, mid-1)
        node.right = self.__make_tree(list, mid+1, end)
        return node


class Test(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.insert(5)
        self.bst.insert(7)
        self.bst.insert(3)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.mbst = MinimalTree()
    
    def test_bst_pre_order(self):
        self.assertEqual(self.bst.show(), [5, 3, 2, 7, 6, 8])

    def test_minimal_tree(self):
        self.mbst.make_tree([2, 4, 6, 7, 8, 9])
        self.assertEqual(self.mbst.show(), [6, 2, 4, 8, 7, 9])

if __name__ == "__main__":
    unittest.main()