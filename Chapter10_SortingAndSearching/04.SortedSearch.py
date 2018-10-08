"""Sorted Search, No Size

You are given an array-like data structure Listy which lacks a size
method. It does, however, have an elementAt (i) method that returns the element at index i in
0(1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
find the index at which an element x occurs. If x occurs multiple times, you may return any index.

Hints: 
#320
Think about how binary search works. What will be the issue with just implementing
binary search?
#337
Binary search requires comparing an element to the midpoint. Getting the midpoint
requires knowing the length. We don't know the length. Can we find it?
#348
We can find the length by using an exponential backoff. First check index 2, then 4, then
8, then 16, and so on. What will be the runtime of this algorithm?
"""

def find_element(array, element):
    last_index = 1
    while array[last_index] != -1 and array[last_index] < element:
        last_index *= 2
    first_index = 0
    result = False
    while not result and first_index <= last_index:
        mid = (first_index + last_index) // 2        
        if element == array[mid]:
            result = True
        elif array[mid] == -1 or element < array[mid]:
            last_index = mid - 1
        else:
            first_index = mid + 1
    return result

class Listy:
    def __init__(self, array):
        self.array = array
    
    def __getitem__(self, index):
        if index < len(self.array):
            return self.array[index]
        else:
            return -1

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.array = Listy([1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25])
    
    def test_find_element(self):
        self.assertTrue(find_element(self.array, 5))
        self.assertTrue(find_element(self.array, 1))
        self.assertTrue(find_element(self.array, 15))
        self.assertTrue(find_element(self.array, 20))
        self.assertTrue(find_element(self.array, 25))
        self.assertTrue(find_element(self.array, 7))
        self.assertTrue(find_element(self.array, 10))


if __name__ == "__main__":
    unittest.main()
