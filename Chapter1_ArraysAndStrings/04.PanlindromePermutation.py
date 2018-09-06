"""Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)

"""

from collections import Counter

def checkPelindrome(string):
    charCount = Counter(string.lower())
    del charCount[" "]
    checkedOdd = 0    
    
    for value in charCount.values():
        if value % 2:
            checkedOdd += 1
    
    return True if checkedOdd < 2 else False

if __name__ == '__main__':
    print(checkPelindrome("Tact Coa"))