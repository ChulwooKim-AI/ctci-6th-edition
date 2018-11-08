"""There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false

Hints: 
#23
Start with the easy thing. Can you check each of the conditions separately?
#97
What is the relationship between the "insert character" option and the "remove character"
option? Do these need to be two separate checks?
#130
Can you do all three checks in a single pass?
"""

'''
Using hashtable, we can define edit cases following this:
First case: characters of longer string are not in shorter string
Second case: Even though they have same length, character of one string is not in another one.
Third case: they have a same character but different count.

Time Complexity: O(n)
Space Complexity: O(n)
'''

from collections import Counter

def checkStatus(shorter, longer):
    status = 0
    for letter in longer.keys():
        if letter not in shorter:
            status += 1
        elif shorter[letter] != longer[letter]:
            status += 1
    return status

def compareStrings(source, target):
    status = 0    
    sourceCount = Counter(source)
    targetCount = Counter(target)

    if len(source) > len(target):
        status = checkStatus(targetCount, sourceCount)
    else:
        status = checkStatus(sourceCount, targetCount)
    
    return status == 1


import unittest

class Test(unittest.TestCase):
    def test_compare_string(self):        
        self.assertTrue(compareStrings("pale", "ple"))
        self.assertTrue(compareStrings("pales", "pale"))
        self.assertTrue(compareStrings("pale", "bale"))
        self.assertFalse(compareStrings("pale", "bake"))


if __name__ == "__main__":
    unittest.main()

