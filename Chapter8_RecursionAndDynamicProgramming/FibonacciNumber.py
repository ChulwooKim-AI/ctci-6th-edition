import unittest

'''Method 1

Time complexity : O(2^n)
'''
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

'''Method 2

Time complexity : O(n)
'''
def fibonacci_top_down(n):
    return __fibonacci_top_down(n, {})

def __fibonacci_top_down(n, memo):
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = __fibonacci_top_down(n-1, memo) + __fibonacci_top_down(n-2, memo)
    return memo[n]

'''Method 3

Time complexity : O(n)
'''
def fibonacci_bottom_up(n):
    if n == 0 or n == 1:
        return n
    a = 0
    b = 1
    for _ in range(2, n):
        c = a + b
        a = b
        b = c
    return a + b


class Test(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci_top_down(6), 8)
        self.assertEqual(fibonacci_bottom_up(7), 13)

if __name__ == "__main__":
    unittest.main()