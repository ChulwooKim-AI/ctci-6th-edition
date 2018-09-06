"""Random Node

You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.

Hints: 
#42
Be very careful in this problem to ensure that each node is equally likely and that
your solution doesn't slow down the speed of standard binary search tree algorithms
(like insert, find, and delete). Also, remember that even if you assume that it's a
balanced binary search tree, this doesn't mean that the tree is full /complete/perfect.
#54
This is your own binary search tree class, so you can maintain any information about the
tree structure or nodes that you'd like (provided it doesn't have other negative implications,
like making insert much slower). In fact, there's probably a reason the interview
question specified that it was your own class. You probably need to store some additional
information in order to implement this efficiently.
#62
As a naive "brute force" algorithm, can you use a tree traversal algorithm to implement
this algorithm? What is the runtime of this?
#75
Alternatively, you could pick a random depth to traverse to and then randomly traverse,
stopping when you get to that depth. Think this through, though. Does this work?
#89
Picking a random depth won't help us much. First, there's more nodes at lower depths
than higher depths. Second, even if we re-balanced these probabilities, we could
hit a "dead end" where we meant to pick a node at depth 5 but hit a leaf at depth 3.
Re-balancing the probabilities is an interesting, though.
#99
A naive approach that many people come up with is to pick a random number between
1 and 3. If it's 1, return the current node. If it's 2, branch left. If it's 3, branch right. This
solution doesn't work. Why not? Is there a way you can adjust it to make it work?
#112
The reason that the earlier solution (picking a random number between 1 and 3) doesn't
work is that the probabilities for the nodes won't be equal. For example, the root will be
returned with probability 1/3, even if there are 50+ nodes in the tree. Clearly, not all the
nodes have probability 1/3, so these nodes won't have equal probability. We can resolve
this one issue by picking a random number between 1 and size_of tree instead.
This only resolves the issue for the root, though. What about the rest of the nodes?
#119
The issue with the earlier solution is that there could be more nodes on one side of a
node than the other. So, we need to weight the probability of going left and right based
on the number of nodes on each side. How does this work, exactly? How can we know
the number of nodes?

Comment: Two variables, size and index, are added in the node class. 
The index is an order of insertation to binary tree while the size is the number of children nodes.
This solution can have equally  probability through the variables.
"""

from random import randrange
import unittest

class Node:
    def __init__(self, data=None, index=0):
        self.right = None
        self.left = None
        self.data = data
        self.index = index
        self.size = 0

class ExtendedBinaryTree:
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
                node.right = Node(data, self.root.size+1)                
        else:
            if node.left:
                self.__insert(node.left, data)
            else:
                node.left = Node(data, self.root.size+1)                
        node.size += 1
    
    def get_random_node(self):
        random_number = randrange(self.root.size + 1)              
        return self.__get_random_node(self.root, random_number)
    
    def __get_random_node(self, node, random_number):
        stack = [node]
        while stack:
            current_node = stack.pop()            
            if current_node.index == random_number:                
                return current_node
            else:
                if current_node.left:
                    stack.append(current_node.left)
                if current_node.right:
                    stack.append(current_node.right)
        return None


class Test(unittest.TestCase):
    def setUp(self):
        self.ebt = ExtendedBinaryTree()
        self.ebt.insert(5)
        self.ebt.insert(3)
        self.ebt.insert(8)
        self.ebt.insert(2)
        self.ebt.insert(4)
        self.ebt.insert(7)
        self.ebt.insert(11)
        self.ebt.insert(12)
        self.ebt.insert(13)
    
    def test_random_node(self):        
        self.assertIsNotNone(self.ebt.get_random_node())


if __name__ == "__main__":
    unittest.main()
