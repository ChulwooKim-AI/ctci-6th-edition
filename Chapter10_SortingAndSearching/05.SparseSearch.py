"""Sparse Search

Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.

EXAMPLE
Input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
Output: 4

Hints: 
#256
Try modifying binary search to handle this.
"""

def find_element(array, element):
    first_index = 0
    last_index = len(array) - 1
    while first_index <= last_index:
        mid = (first_index + last_index) // 2        
        move_index = -1
        while array[mid] == "":            
            if mid > first_index:
                mid += move_index            
            else:
                mid = (first_index + last_index) // 2
                move_index = move_index * -1  
                mid += move_index      
            if mid >= last_index:
                return None                
        if element == array[mid]:
            return mid
        elif element < array[mid]:
            last_index = mid - 1
        else:
            first_index = mid + 1
    return None


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    
    def test_find_element(self):
        self.assertEqual(find_element(self.array, "ball"), 4)
        self.assertEqual(find_element(self.array, "at"), 0)
        self.assertEqual(find_element(self.array, "car"), 7)
        self.assertEqual(find_element(self.array, "dad"), 10)
        self.assertEqual(find_element(self.array, "mom"), None)
        self.assertEqual(find_element(self.array, "azur"), None)
        self.assertEqual(find_element(self.array, "cut"), None)

if __name__ == "__main__":
    unittest.main()