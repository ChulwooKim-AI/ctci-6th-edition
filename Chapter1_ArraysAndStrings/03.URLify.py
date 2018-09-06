"""Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"

"""

def urlify(string):
    return string.strip().replace(" ", "%20")

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

if __name__ == '__main__':
    print(urlify2("solve the problem right now    "))

            