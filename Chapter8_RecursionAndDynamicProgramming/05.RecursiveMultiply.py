"""Recursive Multiply

Write a recursive function to multiply two positive integers without using the
* operator. You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.

Hints: 
#166
Think about multiplying 8 by 9 as counting the number of cells in a matrix with width 8
and height 9.
#203
If you wanted to count the cells in an 8x9 matrix, you could count the cells in a 4x9
matrix and then double it.
#227
Think about how you might handle this for odd numbers.
#234
If there's duplicated work across different recursive calls, can you cache it?
#246
If you're doing 9 * 7 (both odd numbers), then you could do 4*7 and 5*7.
#280
Alternatively, if you're doing 9 * 7, you could do 4*7, double that, and then add 7.
"""

'''Method 1

Simple way to multiply using addition

Time Complexity : O(N)
'''
def multiply_without_operation(number1, number2):
    result = 0
    for _ in range(number2):
        result += number1
    return result

'''Method 2

This solution uses recursive function with addition, substraction, and bit shifting.
'''
def recursive_multiply(number1, number2):
    if number1 == 1:
        return number2
    return recursive_multiply(number1 >> 1, number2) + \
        recursive_multiply(number1 - (number1 >> 1), number2)

'''Method 3

It Optimizes method 2 to remove duplicates.
'''
def optimized_recursive_multiply(number1, number2):
    return __optimized_recursive_multiply(number1, number2, {})

def __optimized_recursive_multiply(number1, number2, table):
    if number1 == 1:
        return number2
    if number1 not in table:
        table[number1] = __optimized_recursive_multiply(number1 >> 1, number2, table) + \
            __optimized_recursive_multiply(number1 - (number1 >> 1), number2, table)
    return table[number1]


import unittest

class Test(unittest.TestCase):
    def test_multipy_without_operation(self):
        self.assertEqual(multiply_without_operation(7, 9), 63)
    
    def test_recursive_multiply(self):
        self.assertEqual(recursive_multiply(7, 9), 63)
    
    def test_optimized_recursive_multiply(self):
        self.assertEqual(optimized_recursive_multiply(7, 9), 63)

if __name__ == "__main__":
    unittest.main()