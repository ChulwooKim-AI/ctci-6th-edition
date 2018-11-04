"""Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Hints: 
#44
Try a hash table.
#117
Could a bit vector be useful?
#132
Can you solve it in O(N log N) time? What might a solution like that look like?
"""

'''
The way to use nested_loop

Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def is_unique(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

'''
This is to use hashtable.

Time Complexity: O(n)
Space Complexity: O(n)
'''
from collections import Counter
def is_unique_with_hash(string):
    letters = Counter(string)

    for letter_count in letters.values():
        if letter_count > 1:
            return False
    return True


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.repeated_string = "asdff"
        self.unique_string = "qwert"

    def test_unique_brute_force(self):
        self.assertTrue(is_unique(self.unique_string))
        self.assertFalse(is_unique(self.repeated_string))
        self.assertTrue(is_unique_with_hash(self.unique_string))
        self.assertFalse(is_unique_with_hash(self.repeated_string))


if __name__ == "__main__":
    unittest.main()
