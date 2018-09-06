"""Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

"""

def compressString(string):
    countChar = 1
    checkedCompression = False
    result = ""
    
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            countChar += 1
            checkedCompression = True
        else:
            result += string[i]
            result += str(countChar)
            countChar = 1    
        if i+1 == len(string)-1:            
            result += string[i+1]
            result += str(countChar) 

    return result if checkedCompression else string


if __name__ == "__main__":
    print(compressString("aabcccccaaa"))