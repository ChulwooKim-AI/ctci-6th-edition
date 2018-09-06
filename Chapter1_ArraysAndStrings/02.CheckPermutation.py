"""Given two strings, write a method to decide if one is a permutation of the
other.
"""
def checkPermutation(string1, string2):
    for letter in string1:
        if letter not in string2:
            return False
    return True

def checkPermutation2(string1, string2):
    letters = {}
    for letter in string1:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    for letter in string2:
        if letter not in letters:
            return False
        else:
            letters[letter] -= 1
        if letters[letter] == 0:
            del letters[letter]
    return len(letters) == 0

	

if __name__ == '__main__':
    print(checkPermutation2("assf", "fsas"))
    