"""Find Duplicates

You have an array with all the numbers from 1 to N, where N is at most 32,000. The
array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
available, how would you print all duplicate elements in the array?

Hints: 
#289
Can you use a bit vector?
#315
Consider implementing your own bit vector class. It's a good exercise and an important
part of this problem.
"""

'''Method 1

This is to use bit vector with AND, OR operations.

'''

def find_duplicates(input_numbers):
    OFFSET_SIZE = 32
    bit_vector = [0] * (32000 // OFFSET_SIZE)
    result = list()
    for number in input_numbers:
        if bit_vector[number // OFFSET_SIZE] & (1 << (number % OFFSET_SIZE)) == 0:
            bit_vector[number // OFFSET_SIZE] |= (1 << (number % OFFSET_SIZE))
        else:
            result.append(number)
    return result

'''Method 2

This is exactly same way to method 1.
Only difference is to make class.

'''

class BitSet:
    OFFSET_SIZE = 32
    def __init__(self, size):
        self.bit_vector = [0] * (size // self.OFFSET_SIZE)
    
    def set(self, number):
        self.bit_vector[number // self.OFFSET_SIZE] |= 1 << (number % self.OFFSET_SIZE)
    
    def get(self, number):
        return self.bit_vector[number // self.OFFSET_SIZE] & 1 << (number % self.OFFSET_SIZE) != 0 


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.input_numbers = list()
        for i in range(32000):
            self.input_numbers.append(i)
        self.input_numbers[12345] = 1111
        self.input_numbers[365] = 10240
    
    def test_find_duplicates(self):
        self.assertListEqual(find_duplicates(self.input_numbers), [10240, 1111])

    def test_bitset_class(self):
        bitset = BitSet(32000)
        result = list()
        for number in self.input_numbers:
            if bitset.get(number):
                result.append(number)
            else:
                bitset.set(number)
        self.assertListEqual(result, [10240, 1111])


if __name__ == "__main__":
    unittest.main()
