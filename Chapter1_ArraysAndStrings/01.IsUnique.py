"""Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

"""
def isUnique(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

from collections import Counter
def isUnique2(string):
    letters = Counter(string)

    for letterCount in letters.values():
        if letterCount > 1:
            return False
    return True

if __name__ == "__main__":
    print(isUnique2("asdff"))
