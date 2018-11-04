"""Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

EXAMPLE
Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"

Hints: 
#53
It's often easiest to modify strings by going from the end of the string to the beginning.
#118
You might find you need to know the number of spaces. Can you just count them?
"""

'''
That is the pythonic way.

Time Complexity: O(n)
Space Complexity: O(1)
'''
def urlify(string):
    return string.strip().replace(" ", "%20")

'''
By iterating a string, they put new url on auxilary space.

Time Complexity: O(n)
Space Complexity: O(n)
'''
def urlify2(string):
    result = []    
    for index in range(len(string)-1):
        if string[index] == " " and string[index+1] != " ":
            result.extend(['%','2','0'])
        elif string[index] == " " and string[index+1] == " ":
            continue
        else:
            result.append(string[index])
    return ''.join(result)


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.string = "solve the problem right now    "
    
    def test_urlify(self):
        self.assertEqual(urlify(self.string), "solve%20the%20problem%20right%20now")
        self.assertEqual(urlify2(self.string), "solve%20the%20problem%20right%20now")


if __name__ == '__main__':
    unittest.main()

            