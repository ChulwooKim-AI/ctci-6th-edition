"""Permutations without Dups

Write a method to compute all permutations of a string of unique characters.

Hints: 
#150
Approach 1: Suppose you had all permutations of abc. How can you use that to get all
permutations of abcd?
#185
Approach 1 :The permutations of abc represent all ways of ordering abc. Now, we want
to create all orderings of abcd. Take a specific ordering of abed, such as bdca. This
bdca string represents an ordering of abc, too: Remove the d and you get bca. Given
the string bca, can you create all the "related" orderings that include d, too?
#200
Approach 1: Given a string such as bca, you can create all permutations of abcd that
have {a, b, c} in the order bca by inserting d into each possible location: dbca,
bdca, bcda, bcad. Given all permutations of abc, can you then create all permutations
of abcd?
#267
Approach 1: You can create all permutations of abcd by computing all permutations of
abc and then inserting d into each possible location within those.
#278
Approach 2: If you had all permutations of two-character substrings, could you generate
all permutations of three-character substrings?
#309
Approach 2: To generate a permutation of abcd, you need to pick an initial character. It
can be a, b, c, or d. You can then permute the remaining characters. How can you use
this approach to generate all permutations of the full string?
#335
Approach 2: To generate all permutations of abcd, pick each character (a, b, c, or d)
as a starting character. Permute the remaining characters and prepend the starting
character. How do you permute the remaining characters? With a recursive process that
follows the same logic.
#356
Approach 2: You can implement this approach by having the recursive function pass
back the list of the strings, and then you prepend the starting character to it. Or, you can
push down a prefix to the recursive calls.
"""

'''Method 1

It is the way to find permutation by order of characters

string[0], prev_list, next_list = c, [''], [c]
string[0], prev_list, next_list = b, [c], [bc]
string[0], prev_list, next_list = b, [c], [cb]
string[0], prev_list, next_list = a, [bc, cb], [abc]
string[0], prev_list, next_list = a, [bc, cb], [abc, bac]
string[0], prev_list, next_list = a, [bc, cb], [abc, bac, bca]
string[0], prev_list, next_list = a, [bc, cb], [abc, bac, bca, acb]
'''

def find_permutation(string):
    if len(string) == 0:
        return ['']
    prev_list = find_permutation(string[1:len(string)])
    next_list = []
    for i in range(len(prev_list)):
        for j in range(len(string)):
            new_str = prev_list[i][0:j] + string[0] + prev_list[i][j:len(string)-1]
            
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list


'''Method 2

This is the way to swap two values.

"abc" , index start, i = 2, 2
"acb" , index start, i = 1, 2
"abc" , index start, i = 1, 2
"bac" , index start, i = 0, 1
"bca" , index start, i = 1, 2
'''


def find_permutations_by_swapping(string):
    result = []
    __find_permutations_by_swapping(string, 0, result)
    return result


def __find_permutations_by_swapping(string, start, result):
    if start >= len(string):
        result.append(string)
    else:
        for i in range(start, len(string)):
            string = swap(string, start, i)
            __find_permutations_by_swapping(string, start+1, result)
            string = swap(string, start, i)


def swap(string, i, j):
    temp = string[i]
    string = string[:i] + string[j] + string[i+1:]
    string = string[:j] + temp + string[j+1:]
    return string


'''Method 3

With seperating to prefix and suffix, it makes permutation.

("", "abc")
("a", "bc")
("ab", "c")
("ac", "b")
("abc", "")
("acb", "")
'''


def find_permutations_by_recursion(string):
    result = []
    __find_permutations_by_recursion("", string, result)
    return result


def __find_permutations_by_recursion(prefix, suffix, result):
    if not len(suffix):
        result.append(prefix)
    else:
        for i in range(len(suffix)):
            __find_permutations_by_recursion(
                prefix+suffix[i], suffix[:i]+suffix[i+1:], result)


import unittest


class Test(unittest.TestCase):
    def test_swap_permutation(self):
        self.assertListEqual(find_permutations_by_swapping("abc"),
                             ['abc', 'acb', 'bac', 'bca', 'cba', 'cab'])

    def test_recursive_permutation(self):
        self.assertListEqual(find_permutations_by_recursion("abc"),
                             ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    
    def test_permutation(self):
        self.assertListEqual(find_permutation("abc"),
                             ['abc', 'bac', 'bca', 'acb', 'cab', 'cba'])


if __name__ == "__main__":
    unittest.main()
