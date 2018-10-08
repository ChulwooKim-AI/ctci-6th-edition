"""Group Anagrams

Write a method to sort an array of strings so that all the anagrams are next to
each other.

Hints: 
#177
How do you check if two words are anagrams of each other? Think about what the definition
of "anagram" is. Explain it in your own words.
#182
Two words are anagrams if they contain the same characters but in different orders.
How can you put characters in order?
#263
Can you leverage a standard sorting algorithm?
#342
Do you even need to truly "sort"? Or is just reorganizing the list sufficient?
"""

'''Method 1

1. Transform each string to a tuple (sorted string, original string). For instance, “cat” will be mapped to (“act”, “cat”).
2. Sort all the tuples by the sorted string, thus, anagrams are grouped together.
3. Output original strings if they share the same sorted string.

Time Complexity : O(nlogn)

'''

def group_anagrams(input):
    tuple_array = [(sorted(word), word) for word in input]
    tuple_array.sort(key=lambda x: x[0])
    return [pair[1] for pair in tuple_array]


'''Method 2

1. Transform each string to a tuple (sorted string, original string). For instance, “cat” will be mapped to (“act”, “cat”).
2. Save the tuples to hash map.
3. Output original strings if they share the same sorted string.

Time Complexity : O(n)

'''

from collections import defaultdict

def group_anagrams_with_hashmap(input):
    hashmap = defaultdict(list)
    for word in input:
        sorted_word = ''.join(sorted(word))
        hashmap[sorted_word].append(word)        
    return [value for value in hashmap.values()]


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.input = ['cat', 'door', 'act', 'dog', 'odor']

    def test_group_anagram_with_sorting(self):
        self.assertListEqual(group_anagrams(self.input), ['cat', 'act', 'dog', 'door', 'odor'])

    def test_group_anagram_with_hashmap(self):
        self.assertListEqual(group_anagrams_with_hashmap(self.input), [['cat', 'act'], ['door', 'odor'], ['dog']])

if __name__ == "__main__":
    unittest.main()
