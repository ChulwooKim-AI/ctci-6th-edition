"""Check Subtree

T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.

Hints: 
#4
If T2 is a subtree of Tl, how will its in-order traversal compare to Tl's? What about its
pre-order and post-order traversal?
#11 
The in-order traversals won't tell us much. After all, every binary search tree with the
same values (regardless of structure) will have the same in-order traversal. This is what
in-order traversal means: contents are in-order. (And if it won't work in the specific case
of a binary search tree, then it certainly won't work for a general binary tree.) The preorder
traversal, however, is much more indicative.
#18 
You may have concluded that if T2. preorderTraversal () is a substring of
Tl. preorderTraversal (), then T2 is a subtree of Tl. This is almost true, except
that the trees could have duplicate values. Suppose Tl and T2 have all duplicate values
but different structures. The pre-order traversals will look the same even though T2 is
not a subtree of Tl. How can you handle situations like this?
#31
Although the problem seems like it stems from duplicate values, it's really deeper than
that. The issue is that the pre-order traversal is the same only because there are null
nodes that we skipped over (because they're null ). Consider inserting a placeholder
value into the pre-order traversal string whenever you reach a null node. Register the
null node as a "real " node so that you can distinguish between the different structures.
#37
Alternatively, we can handle this problem recursively. Given a specific node within T1,
can we check to see if its subtree matches T2?
"""

from BinaryTree import BinaryTree
import unittest

'''Method 1

It can be checked if two trees are same values or not by using pre order checking.
'''
def check_subtree(tree1, tree2):
    node = find_node(tree1.root, tree2.root)    
    tree1_order = pre_order(node, path=[])
    tree2_order = pre_order(tree2.root, path=[])    
    if tree1_order[:len(tree2_order)] == tree2_order:
        return True    
    else:
        return False

def find_node(tree1_node, tree2_node):
    stack = [tree1_node]
    while stack:
        node = stack.pop()
        if node.data == tree2_node.data:
            return node
        else:
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return None        

def pre_order(node, path):
    if node:
        path.append(node.data)        
        pre_order(node.left, path)
        pre_order(node.right, path)
    else:        
        path.append(None)   # added None value in the path to check structure.
    return path

'''Method 2

In order to compare their structure as well as values, 
it should be checked all nodes from same starting point one by one.

'''

def check_subtree_one_by_one(tree1, tree2):
    if tree1 is None and tree2 is None:
        return False
    elif tree2.root is None:
        return True
    else:
        return __check_subtree_one_by_one(tree1.root, tree2.root)

def __check_subtree_one_by_one(tree1_node, tree2_node):
    if tree1_node is None:
        return False
    if tree1_node.data == tree2_node.data:
        return __check_equality(tree1_node, tree2_node)
    else:
        return __check_subtree_one_by_one(tree1_node.left, tree2_node) \
            or __check_subtree_one_by_one(tree1_node.right, tree2_node)

def __check_equality(tree1_node, tree2_node):
    if tree1_node is None and tree2_node is None:
        return True
    elif tree1_node is None or tree2_node is None:
        return False
    elif tree1_node.data == tree2_node.data:
        return __check_equality(tree1_node.left, tree2_node.left) \
            and __check_equality(tree1_node.right, tree2_node.right)
    else:
        return False


class Test(unittest.TestCase):
    def setUp(self):
        self.bst1 = BinaryTree()
        self.bst1.insert(5)
        self.bst1.insert(3)
        self.bst1.insert(7)
        self.bst1.insert(4)
        self.bst1.insert(9)
        self.bst1.insert(6)
            
    def test_check_subtree(self):
        bst2 = BinaryTree()
        bst2.insert(7)
        bst2.insert(9)
        bst2.insert(6)
        self.assertTrue(check_subtree(self.bst1, bst2))
        bst3 = BinaryTree()
        bst3.insert(5)
        bst3.insert(3)
        bst3.insert(6)
        bst3.root.right.data = 4        
        self.assertFalse(check_subtree(self.bst1, bst3))
    
    def test_check_subtree_one_by_one(self):
        bst2 = BinaryTree()
        bst2.insert(7)
        bst2.insert(9)
        bst2.insert(6)
        self.assertTrue(check_subtree_one_by_one(self.bst1, bst2))
        bst3 = BinaryTree()
        bst3.insert(5)
        bst3.insert(3)
        bst3.insert(6)
        bst3.root.right.data = 4        
        self.assertFalse(check_subtree_one_by_one(self.bst1, bst3))

if __name__ == "__main__":
    unittest.main()