"""Rank from Stream

Imagine you are reading in a stream of integers. Periodically, you wish to be able
to look up the rank of a number x (the number of values less than or equal to x). 
Implement the data structures and algorithms to support these operations. 
That is, implement the method track (int x), which is called when each number is generated, 
and the method getRankOfNumber(int x), which returns the number of values less than or 
equal to X (not including x itself).

EXAMPLE
Stream(inorderofappearance) : 5, 1, 4, 4, 5, 9, 7, 13, 3
getRankOfNumber(1) = 0
getRankOfNumber(3) = 1
getRankOfNumber(4) = 3

Hints: 
#301
The problem with using an array is that it will be slow to insert a number. What other
data structures could we use?
#376
When you do a binary subtraction, you flip the rightmost 0s to a 1, stopping when you
get to a 1 (which is al so flipped). Everything (all the 1 s and 0s) on the left will stay put.
#392
Consider a binary search tree where each node stores some additional data.
"""
'''Method 1

Time complexity:
    # Track: O(log(n))
    # Get Rank: O(n)
Space complexity: O(n)
'''
class Node_v1:    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree_v1(object):
    
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = Node_v1(data)
        else:
            self.root = self.__insert(self.root, data)

    def __insert(self, x, data):
        if x is None:
            return Node_v1(data)
        if data <= x.data:
            x.left = self.__insert(x.left, data)
        else:
            x.right = self.__insert(x.right, data)
        return x

    def get_rank_of_number(self, data):
        if self.root is None:
            return None
        return self.__get_rank_of_number(self.root, data)

    def __get_rank_of_number(self, x, data, found=False):
        if x is None:
            return 0
        if data <= x.data and not found:
            if data == x.data:
                found = True
            return self.__get_rank_of_number(x.left, data, found)
        elif data <= x.data:
            return 1 + self.__get_rank_of_number(x.left, data, found)
        else:
            return 1 + self.__get_rank_of_number(x.left, data, found) \
                     + self.__get_rank_of_number(x.right, data, found)

'''Method 2

Time complexity:
    # Track:    O(log(n))
    # Get Rank: O(log(n))
Space complexity: O(n)
'''
class Node_v2:
    def __init__(self, data, left_size=0):
        self.data = data
        self.left = None
        self.right = None
        self.left_size = left_size

class BinarySearchTree_v2:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, data):
        if self.root is None:
            self.root = Node_v2(data)
        else:
            self.root = self.__insert(self.root, data)
    
    def __insert(self, current_node, data):
        if current_node is None:
            return Node_v2(data)
        if data <= current_node.data:
            current_node.left = self.__insert(current_node.left, data)
            current_node.left_size += 1
        else:
            current_node.right = self.__insert(current_node.right, data)
        return current_node
    
    def get_rank_of_number(self, data):
        if self.root is None:
            return None
        return self.__get_rank_of_number(self.root, data)
    
    def __get_rank_of_number(self, current_node, data):
        if current_node is None:
            return None
        if data == current_node.data:
            return current_node.left_size
        elif data < current_node.data:
            return self.__get_rank_of_number(current_node.left, data)
        else:
            right_size = self.__get_rank_of_number(current_node.right, data)
            if right_size is None:
                return None
            return current_node.left_size + 1 + right_size


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.bst_v1 = BinarySearchTree_v1()
        self.bst_v2 = BinarySearchTree_v2()
        stream = [ 5, 1, 4, 4, 5, 9, 7, 13, 3 ]
        for data in stream:
            self.bst_v1.insert(data)
            self.bst_v2.insert(data)
    
    def test_rank_from_stream_v1(self):
        self.assertEqual(self.bst_v1.get_rank_of_number(4), 3)
        self.assertEqual(self.bst_v1.get_rank_of_number(5), 5)
        self.assertEqual(self.bst_v1.get_rank_of_number(9), 7)
        self.assertEqual(self.bst_v1.get_rank_of_number(7), 6)
        self.assertEqual(self.bst_v1.get_rank_of_number(13), 8)
        self.assertEqual(self.bst_v1.get_rank_of_number(3), 1)
        self.assertEqual(self.bst_v1.get_rank_of_number(1), 0)

    def test_rank_from_stream_v2(self):
        self.assertEqual(self.bst_v2.get_rank_of_number(4), 3)
        self.assertEqual(self.bst_v2.get_rank_of_number(5), 5)
        self.assertEqual(self.bst_v2.get_rank_of_number(9), 7)
        self.assertEqual(self.bst_v2.get_rank_of_number(7), 6)
        self.assertEqual(self.bst_v2.get_rank_of_number(13), 8)
        self.assertEqual(self.bst_v2.get_rank_of_number(3), 1)
        self.assertEqual(self.bst_v2.get_rank_of_number(1), 0)


if __name__ == "__main__":
    unittest.main()