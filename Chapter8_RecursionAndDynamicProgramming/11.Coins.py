"""Coins

Given an innnite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.

Hints: 
#300
Try breaking it down into subproblems. If you were making change, what is the first
choice you would make?
#324
If you were making change, the first choice you might make is how many quarters you
need to use.
#343
Once you've decided to use two quarters to make change for 98 cents, you now need
to figure out how many ways to make change for 48 cents using nickels, dimes, and
pennies.
#380
Analyze your algorithm. Is there any repeated work? Can you optimize this?
#394
Try using memoization.
"""

def get_ways_to_make_coins(cent):
    coins = [25, 10, 5, 1]
    return __get_ways_to_make_coins(cent, coins, 0)

def __get_ways_to_make_coins(cent, coins, result):
    if cent == 0:
        return result + 1    
    for index, coin in enumerate(coins):
        if cent - coin < 0:
            continue
        else:
            result = __get_ways_to_make_coins(cent-coin, coins[index:], result)
    return result
        

import unittest

class Test(unittest.TestCase):
    def test_make_change(self):
        self.assertEqual(get_ways_to_make_coins(15), 6)
        self.assertEqual(get_ways_to_make_coins(53), 49)


if __name__ == "__main__":
    unittest.main()