"""Paths with Sum

You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

Hints: 
#6
Try simplifying the problem. What if the path had to start at the root?
#14
Don't forget that paths could overlap. For example, if you're looking for the sum 6, the
paths 1->3->2 and 1->3->2->4->-6->2 are both valid.
#52
If each path had to start at the root we could traverse all possible paths starting from
the root. We can track the sum as we go, incrementing totalPaths each time we
find a path with our target sum. Now, how do we extend this to paths that can start
anywhere? Remember: Just get a brute-force algorithm done. You can optimize later.
#68
To extend this to paths that start anywhere, we can just repeat this process for all nodes.
#77
If you've designed the algorithm as described thus far, you'll have an O(N log N)
algorithm in a balanced tree. This is because there are N nodes, each of which is at depth
O(log N) at worst. A node is touched once for each node above it. Therefore, the N
nodes will be touched O(log N) time. There is an optimization that will give us an
O(N) algorithm.
#87
What work is duplicated in the current brute-force algorithm?
#94
Consider each path that starts from the root (there are N such paths) as an array. What
our brute-force algorithm is really doing is taking each array and finding all contiguous
subsequences that have a particular sum. We're doing this by computing all subarrays
and their sums. It might be useful to just focus on this little subproblem. Given an array,
how would you find all contiguous subsequences with a particular sum? Again, think
about the duplicated work in the brute-force algorithm.
#103 
We are looking for subarrays with sum targetSum. Observe that we can track in
constant time the value of runningSum_1, where this is the sum from element 0 through
element i. For a subarray of element i through element j to have sum targetSum,
runningSum_1-1 + targetSum must equal runningSum_j (try drawing a picture of
an array or a number line). Given that we can track the runningSum as we go, how can
we quickly look up the number of indices i where the previous equation is true?
#108
Try using a hash table that maps from a runningSum value to the number of elements
with this runningSum.
#115
Once you've solidified the algorithm to find all contiguous subarrays in an array with a
given sum, try to apply this to a tree. Remember that as you're traversing and modifying
the hash table, you may need to "reverse the damage" to the hash table as you traverse
back up.
"""

import unittest

class Node:
    def __init__(self, data=None):
        self.right = None
        self.left = None
        self.data = data
        self.number_of_children = 0


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            self.__insert(self.root, data)
        else:
            self.root = Node(data)
    
    def __insert(self, node, data):
        if node.left and node.right:
            if node.left.number_of_children <= node.right.number_of_children:
                self.__insert(node.left, data)
            else:
                self.__insert(node.right, data)
        elif node.left:
            node.right = Node(data)
        elif node.right:
            node.left = Node(data)
        else:
            node.left = Node(data)
        node.number_of_children += 1

'''Method1

This way is to use not brute force, but summation from leaf.
'''

def count_paths_with_sum(bst, target_sum):
    if bst is None:
        return 0   
    return __count_paths_with_sum(bst.root, [], 0, target_sum)

def __count_paths_with_sum(node, path, total_num, target_sum):
    if node is None:
        return total_num
    path.append(node.data)
    total_num = __count_paths_with_sum(node.left, path, total_num, target_sum)
    total_num = __count_paths_with_sum(node.right, path, total_num, target_sum)
    subsum = 0    
    for i in range(len(path)-1, -1, -1):
        subsum += path[i]        
        if subsum == target_sum:         
            total_num += 1            
    path.pop()
    return total_num


'''Method2
This solution use hashtable.

'''
def count_paths_with_sum_by_hashtable(bst, target_sum):
    if bst is None:
        return 0   
    return __count_paths_with_sum_by_hashtable(bst.root, {0: 1}, 0, target_sum)

def __count_paths_with_sum_by_hashtable(node, paths, running_sum, target_sum):
    if node is None:
        return 0    
    running_sum += node.data
    paths[running_sum] = 1 if running_sum not in paths else paths.get(running_sum) + 1    
    current_sum = running_sum - target_sum
    total_num = 0 if current_sum not in paths else paths.get(current_sum)    
    total_num += __count_paths_with_sum_by_hashtable(node.left, paths, running_sum, target_sum)    
    total_num += __count_paths_with_sum_by_hashtable(node.right, paths, running_sum, target_sum)    
    paths[running_sum] -= 1
    return total_num

class Test(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree()
        self.bt.insert(3) 
        self.bt.insert(1)
        self.bt.insert(2)
        self.bt.insert(-3)
        self.bt.insert(1)
        self.bt.insert(4)
        self.bt.insert(-2)
    
    def test_count_paths(self):
        self.assertEqual(count_paths_with_sum(self.bt, 5), 2)
        self.assertEqual(count_paths_with_sum(self.bt, 3), 3)

    def test_count_paths_with_hashtable(self):
        self.assertEqual(count_paths_with_sum_by_hashtable(self.bt, 5), 2)
        self.assertEqual(count_paths_with_sum_by_hashtable(self.bt, 3), 3)

if __name__ == "__main__":
    unittest.main()