"""Magic Index

A magic index in an array A [e ... n -1] is defined to be an index such that A[i] = i. 
Given a sorted array of distinct integers, 
write a method to find a magic index, if one exists, in array A.

FOLLOW UP
What if the values are not distinct?

Hints: 
#170
Start with a brute force algorithm.
#204
Your brute force algorithm probably ran in O(N) time. If you're trying to beat that
runtime, what runtime do you think you will get to? What sorts of algorithms have that
runtime?
#240 
Can you solve the problem in O(log N)?
#286
Binary search has a runtime of O( log N) . Can you apply a form of binary search to the
problem?
#340
Given a specific index and value, can you identify if the magic index would be before or
after it?
"""

import unittest

'''Method 1

This is simple solution by brute force.
Time Complexity : O(N)
'''
def find_index_by_brute_force(array):
    if array is None:
        return None
    for index in range(len(array)):
        if array[index] == index:
            return index
    return None

'''Method 2

This is recursive solution to optimize method 1.
Time complexity : O(logN)
'''
def find_index_by_recursion(array):
    if array is None:
        return None
    return __find_index_by_recursion(array, 0, len(array)-1)

def __find_index_by_recursion(array, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return __find_index_by_recursion(array, mid+1, high)
    else:
        return __find_index_by_recursion(array, low, mid-1)

'''Follow up

It cannot compare value of array to index 
because value of array doesn't guarantee bigger and smaller to index.
For example, [-1, 2, 2, 2, 2, 2] even though value of index 3 is smaller than index 3, 
it is possible to have same value between index 2 and value of index 2.
'''
def find_index_in_duplicates(array):
    if array is None:
        return None
    return __find_index_in_duplicates(array, 0, len(array)-1)

def __find_index_in_duplicates(array, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if array[mid] == mid:
        return mid
    right = __find_index_in_duplicates(array, max(mid+1, array[mid]), high)
    if right:
        return right
    return __find_index_in_duplicates(array, low, min(mid-1, array[mid]))

class Test(unittest.TestCase):
    def setUp(self):
        self.array_distinct = [-1, 0, 1, 2, 3, 5]
        self.array_duplicates = [-1, 0, 0, 0, 2, 7, 7, 7, 10]
    
    def test_find_index(self):
        self.assertEqual(find_index_by_brute_force(self.array_distinct), 5)
        self.assertEqual(find_index_by_recursion(self.array_distinct), 5)
        self.assertEqual(find_index_in_duplicates(self.array_duplicates), 7)


if __name__ == "__main__":
    unittest.main()
