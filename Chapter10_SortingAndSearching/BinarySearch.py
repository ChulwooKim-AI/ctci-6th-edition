def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


import unittest

class Test(unittest.TestCase):
    def test_binary_search(self):
        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        self.assertFalse(binary_search(testlist, 3))
        self.assertTrue(binary_search(testlist, 13))


if __name__ == "__main__":
    unittest.main()