"""Sorted Merge

You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.

Hints: #332
Try moving from the end of the array to the beginning.
"""


def sorted_merge(a, b):
    for i in range(len(b)):
        for j in range(len(a)):            
            if a[j] and a[j] > b[i]:
                a = a[:j] + [b[i]] + a[j:len(a)-1]
                break
            elif a[j] is None:
                a = a[:j] + b[i:]
    return a


import unittest

class Test(unittest.TestCase):
    def test_sorted_merge(self):
        a = [2, 4, 8, 10, None, None, None, None]
        b = [1, 3, 7, 21]
        self.assertListEqual(sorted_merge(a, b), [1, 2, 3, 4, 7, 8, 10, 21])


if __name__ == "__main__":
    unittest.main()