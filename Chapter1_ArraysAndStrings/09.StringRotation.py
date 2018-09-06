"""String Rotation

Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
"""

def is_roatation1(s1, s2):        
    return True if s2 in s1+s1 else False

def is_roatation2(s1, s2):        
    return is_substring(s1+s1, s2)

def is_substring(s1, s2):
    if len(s2) > len(s1):
        return False
    s2point = 0
    for i in range(len(s1)):
        for j in range(len(s2)):            
            if s1[i+j+s2point] != s2[j+s2point] and j == 0:
                break
            elif s1[i+j+s2point] != s2[j+s2point] and j != 0:
                s2point = j
                break
            elif s1[i+j+s2point] == s2[j+s2point] and j+s2point == len(s2)-1:
                return True
    return False

import unittest
class Test(unittest.TestCase):
    def test_is_substring(self):
        s1 = "waterbottle"
        s2 = "erbottl"
        s3 = "Whole Food Market"
        s4 = "ood"
        self.assertEqual(is_substring(s1, s2), True)
        self.assertEqual(is_substring(s3, s4), True)
    
    def test_is_rotation1(self):
        s1 = "waterbottle"
        s2 = "erbottlewat"
        self.assertEqual(is_roatation1(s1, s2), True)

    def test_is_rotation2(self):
        s1 = "waterbottle"
        s2 = "erbottlewat"
        self.assertEqual(is_roatation2(s1, s2), True)
    
if __name__ == "__main__":
    unittest.main()