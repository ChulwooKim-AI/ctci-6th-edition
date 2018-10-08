"""Search in Rotated Array

Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.

EXAMPLE
Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)

Hints: 
#298
Can you modify binary search for this purpose?
#310
What is the runtime of your algorithm? What will happen if the array has duplicates?
"""

def find_element(array, element):
    first = 0
    last = len(array) - 1
    result = False

    while not result and first <= last:
        mid = (first + last) // 2        
        if array[mid] == element:
            result = True
        else:
            if array[first] > array[mid]:
                if array[first] <= element or element < array[mid]:
                    last = mid - 1
                elif array[mid] < element or element <= array[last]:
                    first = mid + 1
            else:
                if element < array[mid]:
                    last = mid - 1
                elif element > array[mid]:
                    first = mid + 1
    return result


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    
    def test_find_element(self):
        self.assertTrue(find_element(self.array, 1))
        self.assertTrue(find_element(self.array, 19))
        self.assertTrue(find_element(self.array, 4))
        self.assertTrue(find_element(self.array, 7))
        self.assertTrue(find_element(self.array, 10))
        self.assertTrue(find_element(self.array, 15))
        self.assertTrue(find_element(self.array, 14))
        self.assertTrue(find_element(self.array, 20))


if __name__ == "__main__":
    unittest.main()
