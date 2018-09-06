"""There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false
"""

from collections import Counter

def checkStatus(shorter, longer):
    status = 0
    for letter in longer.keys():
        if letter not in shorter:
            status += 1
        elif shorter[letter] != longer[letter]:
            status += 1
    return status

def compareStrings(source, target):
    status = 0
    
    sourceCount = Counter(source)
    targetCount = Counter(target)

    if len(source) > len(target):
        status = checkStatus(targetCount, sourceCount)
    else:
        status = checkStatus(sourceCount, targetCount)
    return True if status == 1 else False

if __name__ == "__main__":
    print(compareStrings("pale", "bake"))

