"""Permutations with Dups

Write a method to compute all permutations of a string whose characters
are not necessarily unique. The list of permutations should not have duplicates.

Hints: 
#161
You could handle this by just checking to see if there are duplicates before printing
them (or adding them to a list). You can do this with a hash table. In what case might this
be okay? In what case might it not be a very good solution?
#190
If you haven't solved 8.7 yet, do that one first.
#222
Try getting the count of each character. For example, ABCAAC has 3 As, 2 Cs, and 1 B.
#255
To get all permutations with 3 As, 2 Cs, and 1 B, you need to first pick a starting character:
A, B, or C If it's an A, then you need all permutations with 2 As, 2 Cs, and 1 B.
"""

from collections import Counter

def find_permutation(string):
    string = list(string)
    char_frequency = Counter(string)
    permutation = list()
    result = list()
    __find_permutation([], len(string), char_frequency, permutation)
    for i in permutation:
        result.append(''.join(i))
    return result

def __find_permutation(string, remains, char_frequency, permutation):
    if remains == 0:
        permutation.append(string)
        return
    for char in char_frequency:
        if char_frequency[char] > 0:
            string_copy = string.copy()
            string_copy.append(char)
            char_frequency[char] -= 1
            __find_permutation(string_copy, remains-1, char_frequency, permutation)
            char_frequency[char] += 1


import unittest

class Test(unittest.TestCase):
    def test_find_permutation(self):
        self.assertListEqual(find_permutation("aab"), ['aab', 'aba', 'baa'])


if __name__ == "__main__":
    unittest.main()