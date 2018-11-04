"""Given two strings, write a method to decide if one is a permutation of the
other.

Hints: 
#1
Describe what it means for two strings to be permutations of each other. Now, look at
that definition you provided. Can you check the strings against that definition?
#84
There is one solution that is 0 (N log N) time. Another solution uses some space, but
is O(N) time.
#122
Could a hash table be useful?
#131
Two strings that are permutations should have the same characters, but in different
orders. Can you make the orders the same?
"""

'''
Sort two strings and compare them if they have same characters at same index.

Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False        
    sorted_string1 = sorted([letter for letter in string1])
    sorted_string2 = sorted([letter for letter in string2])

    for i in range(len(sorted_string1)):
        if sorted_string1[i] != sorted_string2[i]:
            return False
    return True

'''
If you use hashtable, you can reduce time complexity.

Time Complexity: O(n)
Space Complexity: O(n)
'''
def check_permutation_with_hash(string1, string2):
    letters = {}
    for letter in string1:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    for letter in string2:
        if letter not in letters:
            return False
        else:
            letters[letter] -= 1
        if letters[letter] == 0:
            del letters[letter]
    return len(letters) == 0

	
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.string1 = "assf"
        self.string2 = "fsas"
        self.string3 = "fasas"
    
    def test_check_permutation(self):
        self.assertTrue(check_permutation(self.string1, self.string2))
        self.assertTrue(check_permutation_with_hash(self.string1, self.string2))
        self.assertFalse(check_permutation(self.string1, self.string3))
        self.assertFalse(check_permutation_with_hash(self.string1, self.string3))


if __name__ == '__main__':
    unittest.main()
    