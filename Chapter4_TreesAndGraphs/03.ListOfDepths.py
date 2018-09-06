"""List of Depths 

Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).

Hints: 
#107
Try modifying a graph search algorithm to track the depth from the root.
#123
A hash table or array that maps from level number to nodes at that level might also be
useful.
#135
You should be able to come up with an algorithm involving both depth-first search and
breadth-first search.
"""

from collections import defaultdict
from BinaryTree import BinaryTree
import unittest

def list_of_depths(bst):
    depth = 0
    queue = [(bst.root, depth)]
    depth_list = defaultdict(list)
    
    while queue:
        current_node, current_depth = queue.pop(0)        
        depth_list[current_depth].append(current_node.data)
        if current_node.left:
            queue.append((current_node.left, current_depth+1))                
        if current_node.right:
            queue.append((current_node.right, current_depth+1))
                
    return depth_list

class Test(unittest.TestCase):
    def setUp(self):
        self.bst = BinaryTree()
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(4)
        self.bst.insert(2)
        self.bst.insert(1)
        self.bst.insert(6)
        self.bst.insert(9)
        self.bst.insert(7)
        self.bst.insert(8)
        
    def test_depth_list(self):                
        result = list_of_depths(self.bst)        
        self.assertEqual(result.get(0), [5])
        self.assertEqual(result.get(1), [3, 6])
        self.assertEqual(result.get(2), [2, 4, 9])
        self.assertEqual(result.get(3), [1, 7])
        self.assertEqual(result.get(4), [8])

if __name__ == "__main__":
    unittest.main()

"""
     5
   3    6
  2  4    9
1       7
          8
"""