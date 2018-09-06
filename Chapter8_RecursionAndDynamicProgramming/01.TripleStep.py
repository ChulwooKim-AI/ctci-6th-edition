"""Triple Step

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.

Hints: 
#152
Approach this from the top down. What is the very last hop the child made?
#178
If we knew the number of paths to each of the steps before step 100, could we compute
the number of steps to 1OO?
#217
We can compute the number of steps to 100 by the number of steps to 99, 98, and 97.
This corresponds to the child hopping 1, 2, or 3 steps at the end. Do we add those or
multiply them?That is: Is it f(100) = f(99) + f(98) + f(97) or f(100) =
f(99) * f(98) * f(97)?
#237
We multiply the values when it's "we do this then this." We add them when it's "we do this or this."
#262
What is the runtime of this method? Think carefully. Can you optimize it?
#359
Try memoization as a way to optimize an inefficient recursive program.
"""

import unittest

def count_way_to_step(number):
    if number == 0:
        return 1
    elif number < 0:
        return 0
    else:
        return count_way_to_step(number-3) + count_way_to_step(number-2) + count_way_to_step(number-1)

def count_way_to_step_by_dynamic(number):
    if number < 1:
        return None
    else:
        return __count_way_to_step_by_dynamic(number, {})

def __count_way_to_step_by_dynamic(number, table):
    if number == 0:
        return 1
    elif number < 0:
        return 0
    if number not in table:
        table[number] = __count_way_to_step_by_dynamic(number-3, table) \
                        + __count_way_to_step_by_dynamic(number-2, table) \
                        + __count_way_to_step_by_dynamic(number-1, table)
    return table[number]


class Test(unittest.TestCase):
    def test_count_way_to_step(self):
        self.assertEqual(count_way_to_step(4), 7)
    
    def test_count_way_to_step_by_dynamic(self):
        self.assertEqual(count_way_to_step_by_dynamic(4), 7)

if __name__ == "__main__":
    unittest.main()