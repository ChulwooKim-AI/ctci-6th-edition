"""BST Sequences

A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.

EXAMPLE
Input:   2
       1   3
Output: {2, 1, 3}, {2, 3, 1}
Hints: 
#39
What is the very first value that must be in each array?
#48
The root is the very first value that must be in every array. What can you say about the
order of the values in the left subtree as compared to the values in the right subtree? Do
the left subtree values need to be inserted before the right subtree?
#66
The relationship between the left subtree values and the right subtree values is, essentially,
anything. The left subtree values could be inserted before the right subtree, or the
reverse (right values before left), or any other ordering.
#82
Break this down into subproblems. Use recursion. If you had all possible sequences for
the left subtree and the right subtree, how could you create all possible sequences for
the entire tree?
"""

from BinaryTree import BinaryTree
import unittest

def get_sequences(bst):
    return __get_sequences([bst.root])

def __get_sequences(nodes):
    result = []
    for i in range(len(nodes)):
        subtree = nodes.copy()
        current_node = subtree.pop(i)
        print("in:", i,len(nodes), current_node.data, len(subtree))
        if current_node.left:
            subtree.append(current_node.left)
        if current_node.right:
            subtree.append(current_node.right)
        print("len:",len(subtree))
        if len(subtree):            
            for j in __get_sequences(subtree):   
                print("j:",j)
                if isinstance(j, list):             
                    result.append([current_node.data] + j)
                else:
                    result.append([current_node.data] + [j])                       
        else:
            result.append(current_node.data)    
        print("result:",result)
    return result
                

def bst_sequences(bst):
    return bst_sequences_partial([], [bst.root])

def bst_sequences_partial(partial, subtrees):
    if not len(subtrees):
        return [partial]
    sequences = []
    for index, subtree in enumerate(subtrees):        
        next_partial = partial + [subtree.data]
        next_subtrees = subtrees[:index] + subtrees[index+1:]        
        if subtree.left:
            next_subtrees.append(subtree.left)
        if subtree.right:
            next_subtrees.append(subtree.right)
        sequences += bst_sequences_partial(next_partial, next_subtrees)
    return sequences


class Test(unittest.TestCase):
    def setUp(self):
        self.bst = BinaryTree()
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)              
    
    def test_bst_sequences1(self):
        self.assertListEqual(get_sequences(self.bst), [[5, 3, 7], [5, 7, 3]])
        self.bst.insert(6)
        #self.assertListEqual(get_sequences(self.bst), [[5, 3, 7, 6], [5, 7, 3, 6], [5, 7, 6, 3]])        

    def test_bst_sequences2(self):
        self.assertListEqual(bst_sequences(self.bst), [[5, 3, 7], [5, 7, 3]])
        self.bst.insert(6)
        self.bst.insert(4)
        self.assertListEqual(bst_sequences(self.bst), 
                                                        [[5, 3, 7, 4, 6], 
                                                        [5, 3, 7, 6, 4], 
                                                        [5, 3, 4, 7, 6], 
                                                        [5, 7, 3, 6, 4], 
                                                        [5, 7, 3, 4, 6], 
                                                        [5, 7, 6, 3, 4]])
        

if __name__ == "__main__":
    unittest.main()