"""Check Balanced 

Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.

Hints: 
#21
Think about the definition of a balanced tree. Can you check that condition for a single
node? Can you check it for every node?
#33
If you've developed a brute force solution, be careful about its runtime. If you are
computing the height of the subtrees for each node, you could have a pretty inefficient
algorithm.
#49
What if you could modify the binary tree node class to allow a node to store the height
of its subtree?
#105
You don't need to modify the binary tree class to store the height of the subtree. Can
your recursive function compute the height of each subtree while also checking if a
node is balanced? Try having the function return multiple values.
#124
Actually, you can just have a single checkHeight function that does both the height
computation and the balance check. An integer return value can be used to indicate
both.
"""

from BinaryTree import BinaryTree 
import unittest

# Time complexity : O(n^2)
def get_height(node):
    if node is None:
        return 0
    else:
        return max(get_height(node.left), get_height(node.right)) + 1

def is_balanced(bst):
    if bst.root is None:
        return None
    else:
        return __is_balanced(bst.root)

def __is_balanced(node):
    if node is None:
        return True
    left_height = get_height(node.left)
    right_height = get_height(node.right)

    if abs(left_height - right_height) <= 1 and __is_balanced(node.left) and __is_balanced(node.right):
        return True
    else:
        return False

# Time complexity : O(n)
def is_balanced_with_optimization(bst):
    if bst:
        _, is_balanced = __is_balanced_with_optimization(bst.root)
        return is_balanced
    else:
        return None

def __is_balanced_with_optimization(node):
    if node is None:
        return (0, True)
    else:
        left_height, left_balanced = __is_balanced_with_optimization(node.left)
        right_height, right_balanced = __is_balanced_with_optimization(node.right)        
        height = max(left_height, right_height) + 1
        if abs(left_height - right_height) <= 1 and left_balanced and right_balanced:
            return (height, True)
        else:
            return (height, False)


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
        
    def test_balanced_bst(self):
        self.assertTrue(is_balanced(self.bst))
        self.bst.insert(7)
        self.bst.insert(8)
        self.assertFalse(is_balanced(self.bst))
    
    def test_balanced_bst_optimization(self):
        self.assertTrue(is_balanced_with_optimization(self.bst))
        self.bst.insert(7)
        self.bst.insert(8)
        self.assertFalse(is_balanced_with_optimization(self.bst))

if __name__ == "__main__":
    unittest.main()