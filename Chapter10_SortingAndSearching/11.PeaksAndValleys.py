"""Peaks and Valleys

In an array of integers, a "peak" is an element which is greater than or equal to the adjacent 
integers and a "valley" is an element which is less than or equal to the adjacent integers.
For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. 
Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

EXAMPLE
Input: {5, 3, 1, 2, 3}
Output: {5, 1, 3, 2, 3}

Hints: 
#196
Imagine the array were sorted in ascending order. Is there any way you could "fix it" to
be sorted into alternating peaks and valleys?
#219
Try walking through a sorted array. Can you just swap elements until you have fixed the
array?
#231
Note that if you ensure the peaks are in place, the valleys will be, too. Therefore, your
iteration to fix the array can skip over every other element.
#253
Do you necessarily need the arrays to be sorted? Can you do it with an unsorted array?
#277
Suppose you had a sequence of three elements {0, 1, 2}, in any order. Write out all
possible sequences for those elements and how you can fix them to make 1 the peak.
#292
Revisit the set of sequences for {0, 1, 2} that you just wrote out. Imagine there are
elements before the leftmost element. Are you sure that the way you swap the elements
won't invalidate the previous part of the array?
#316
You should be able to design an O(n) algorithm.
"""

'''Method 1

Time Complexity : O(nlogn)
Space Complexity : O(1)

'''
def make_peaks_and_valleys(array):
    array.sort()
    for i in range(1, len(array), 2):
        array[i-1], array[i] = array[i], array[i-1]
    return array


'''Method 2

Time Complexity : O(n)
Space Complexity : O(1)

'''
import sys

def make_peaks_and_valleys_without_sorting(array):
    for i in range(1, len(array), 2):
        biggest_integer = max_integer(array, i-1, i, i+1)
        if i != biggest_integer:
            array[i], array[biggest_integer] = array[biggest_integer], array[i]
    return array

def max_integer(array, prev, curr, _next):
    length = len(array)
    prev_value = array[prev] if prev >= 0 and prev < length else -sys.maxsize - 1
    curr_value = array[curr] if curr >= 0 and curr < length else -sys.maxsize - 1
    next_value = array[_next] if _next >= 0 and _next < length else -sys.maxsize - 1

    max_value = max([prev_value, curr_value, next_value])

    if max_value == prev_value:
        return prev
    elif max_value == curr_value:
        return curr
    else:
        return _next


'''Method 3

Time Complexity : O(n)
Space Complexity : O(1)
'''

def make_peaks_and_valleys_without_sorting_v2(array):
    for i in range(1, len(array), 2):
        if array[i-1] < array[i]:
            array[i-1], array[i] = array[i], array[i-1]
        if i+1 < len(array) and array[i+1] < array[i]:
            array[i+1], array[i] = array[i], array[i+1]
    return array


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.array = [5, 3, 1, 2, 3]
    
    def test_make_peaks_and_valleys(self):
        self.assertListEqual(make_peaks_and_valleys(self.array), [2, 1, 3, 3, 5])
        self.assertListEqual(make_peaks_and_valleys_without_sorting(self.array), [2, 3, 1, 5, 3])
        self.assertListEqual(make_peaks_and_valleys_without_sorting_v2(self.array), [3, 1, 5, 2, 3])


if __name__ == "__main__":
    unittest.main()
