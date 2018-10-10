"""Missing Int

Given an input file with four billion non-negative integers, provide an algorithm to
generate an integer that is not contained in the file. Assume you have 1 GB of memory available for
this task.

FOLLOW UP
What if you have only 10MB of memory? Assume that all the values are distinct and we now have
no more than one billion non-negative integers.

Hints: 
#235
Would a bit vector help?
#254
To do it with less memory, can you try multiple passes?
#281
Try using one pass to get it down to a range of values, and then a second pass to find a
specific value.
"""

'''Method 1

Different non-negative integers can have 2^31 number and 1 GB = 2^33 bits.
Therefore, it is possible to cover all integer number within 1 GB memory
The idea is to save all numbers in a given file to listed 2^31 bits and find 0 in the list.
ex) bit_field[0] = 1111111 <- saved 0,1,2,3,4,5,6,7 
    bit_field[1] = 1111101 <- saved 8,10,11,12,13,14,15 (We can find number 9!)
'''

def find_missing_int(input_file):
    MAX_INTEGER = int((1 << 31) - 1)
    OFFSET_SIZE = 8
    bit_field = [0] * (MAX_INTEGER // OFFSET_SIZE)
    for integer in input_file:
        bit_field[integer // OFFSET_SIZE] |= 1 << (integer % OFFSET_SIZE)    
    for i in range(len(bit_field)):
        for j in range(OFFSET_SIZE):
            if bit_field[i] & (1 << j) == 0:
                return i * OFFSET_SIZE + j
    return None

'''Method 2

Different non-negative integers can have 2^31 number and 10 MB of memory = 2^23 bits
It should be make blocks because 10MB of memory cannot cover all integers.
Thus, unlike method 1 check all integers in bit field, it counts the number of integers in each block
included a range of number.
And find the block with missing integer and make bit field to load to 10 MB of memory.
Then, repeat a same way to Method 1, finding a index of bit field with 0s, and return it.
Ex) blocks[0] = 2^23 (the block has 0~2^23 integer)
    blocks[1] = 2^23 - 1 (the block has 2^23~2^24 integer except for 1 number) 
    bit_vector[0] = 11111111
    bit_vector[1] = 11111101 (This is what we want to find)
'''
MAX_INTEGER = int((1 << 31) - 1)
OFFSET_SIZE = 8

def find_missing_int_with_10mb(input_file):    
    range_size = int(1 << 23)
    blocks = get_count_per_block(input_file, range_size)
    block_index = find_block_with_missing(blocks, range_size)
    if block_index is None:
        return None
    bit_vector = get_bit_vector_for_range(input_file, block_index, range_size)
    offset = find_zero(bit_vector)
    if offset is None:
        return None
    return block_index * range_size + offset

def get_count_per_block(input_file, range_size):
    
    blocks = [0] * (MAX_INTEGER // range_size)
    '''
    with open(input_file, 'r') as numbers:
        for n in numbers:
            blocks[n // range_size] += 1
    '''
    for integer in range(len(input_file)):
        blocks[integer // range_size] += 1
    return blocks

def find_block_with_missing(blocks, range_size):
    for i in range(len(blocks)):
        if blocks[i] < range_size:
            return i
    return None

def get_bit_vector_for_range(input_file, block_index, range_size):
    
    bit_vector = [0] * (range_size // OFFSET_SIZE)
    start_range = block_index * range_size
    end_range = start_range + range_size
    for integer in input_file:
        if integer >= start_range and integer < end_range:
            offset = integer - start_range
            bit_vector[offset // OFFSET_SIZE] |= 1 << (offset % OFFSET_SIZE)
    return bit_vector

def find_zero(bit_vector):
    for i in range(len(bit_vector)):
        for j in range(OFFSET_SIZE):
            if bit_vector[i] & (1 << j) == 0:
                return i * OFFSET_SIZE + j
    return None


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = [0,1,2,3,4,5,8,10,11,12,13,14,15,16,17,19,20]
    
    def test_find_missing_int(self):
        self.assertEqual(find_missing_int(self.input_file), 6)
    
    def test_find_missing_int_with_10mb(self):
        self.assertEqual(find_missing_int_with_10mb(self.input_file), 6)


if __name__ == "__main__":
    unittest.main()
    