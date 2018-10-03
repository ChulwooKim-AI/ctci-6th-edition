def radixsort(alist):
    RADIX = 10
    max_length = False
    tmp = -1
    place = 1
    while not max_length:
        max_length = True
        buckets = [ list() for _ in range(RADIX) ]
        for item in alist:
            tmp = item // place
            buckets[tmp % RADIX].append(item)
            if max_length and tmp > 0:
                max_length = False
        i = 0
        for bucket in buckets:
            for item in bucket:
                alist[i] = item
                i += 1
        place *= RADIX
        print(buckets, alist)


import unittest

class Test(unittest.TestCase):
    def test_radix_sort(self):
        alist = [32,3,2,65,7,43,69,7,21,10,42,70]
        radixsort(alist)
        self.assertListEqual(alist, [2, 3, 7, 7, 10, 21, 32, 42, 43, 65, 69, 70])      


if __name__ == "__main__":
    unittest.main()