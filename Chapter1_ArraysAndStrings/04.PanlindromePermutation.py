"""Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)

Hints: 
#106
You do not have to-and should not-generate all permutations. This would be very inefficient.
#121
What characteristics would a string that is a permutation of a palindrome have?
#134
Have you tried a hash table? You should be able to get this down to 0 (N) time.
#136
Can you reduce the space usage by using a bit vector?
"""

'''
Using hashtable, you can solve the problem comparing with count of each characters.

Time Complexity: O(n)
Space Complexity: O(n)
'''
from collections import Counter

def checkPelindrome(string):
    charCount = Counter(string.lower())
    del charCount[" "]
    checkedOdd = 0    
    
    for value in charCount.values():
        if value % 2:
            checkedOdd += 1
    
    return checkedOdd < 2


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.string1 = "Tact Coa"
        self.string2 = "dogs god"
    
    def test_check_panlindrome(self):
        self.assertTrue(checkPelindrome(self.string1))
        self.assertTrue(checkPelindrome(self.string2))


if __name__ == '__main__':
    unittest.main()