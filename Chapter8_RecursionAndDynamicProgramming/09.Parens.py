"""Parens

Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n pairs of parentheses.

EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()

Hints: 
#138
Try the Base Case and Build approach.
#174
Suppose we had all valid ways of writing two pairs of parentheses. How could we use
this to get all valid ways of writing three pairs?
#187
We could try generating the solution for three pairs by taking the list of two pairs of
parentheses and adding a third pair. We'd have to add the third paren before, around,
and after. That is: ()<SOLUTION>, (<SOLUTION>), <SOLUTION>(). Will this work?
#209
The problem with the solution suggested by the earlier hint is that it might have duplicate
values. We could eliminate this by using a hash table.
#243
Alternatively, we could think about doing this by moving through the string and adding
left and right parens at each step. Will this eliminate duplicates? How do we know if we
can add a left or right paren?
#265
Adding a left or right paren at each step will eliminate duplicates. Each substring will be
unique at each step. Therefore, the total string will be unique.
#295
We can ensure that this string is valid by counting the number of left and right parens.
It is always valid to add a left paren, up until the total number of pairs of parens. We can
add a right paren as long as count (left parens) < = count (right parens) .
"""

'''Method 1

It adds a parenthes to front and back of subset and wraps the subset through a parenthes.
Also, duplicates can be eliminated by hashtable
'''
def get_parens(number):
    result = {}
    __get_parens(number, result)    
    return list(result.keys())

def __get_parens(number, result):
    if number == 1:
        result["()"] = 0
        return 
    __get_parens(number-1, result)
    temp = result.copy()    
    for item in temp:
        result["()" + item] = 0
        result["(" + item + ")"] = 0
        result[item + "()"] = 0
        del result[item]

'''Method 2

This finds all parentheses by moving through the string and adding
left and right parens at each step.
'''
def get_parens_by_moving(number):
    result = list()
    __get_parens_by_moving(number, 0, 0, [], result)
    return result

def __get_parens_by_moving(number, left, right, string, result):
    if len(string) == 2*number:
        result.append(''.join(string))
        return
    if left < number:
        temp = string.copy()
        temp.append('(')
        __get_parens_by_moving(number, left+1, right, temp, result)
    if right < left:
        temp = string.copy()
        temp.append(')')
        __get_parens_by_moving(number, left, right+1, temp, result)


import unittest

class Test(unittest.TestCase):
    def test_parens_by_moving(self):
        self.assertListEqual(get_parens_by_moving(3), \
                ['((()))', '(()())', '(())()', '()(())', '()()()'])
        self.assertListEqual(get_parens(3), \
                ['()()()', '(()())', '()(())', '((()))', '(())()'])


if __name__ == "__main__":
    unittest.main()