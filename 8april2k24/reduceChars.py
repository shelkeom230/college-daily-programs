# Date - 08/04/2024
# Que. 24

# Given a string with multiple characters that are repeated consecutively, reduce the size of the string using mathematical logic. Replace consecutive repeated characters with the character followed by the count of repetitions.

# Input: aabbbbeeeeffggg

# Output: a2b4e4f2g3

def reduceChar(s):
    if not s:
        return ""

    count=1
    reduceChar=""
    currentChar=s[0]

    for i in range(1,len(s)):
        if s[i]==currentChar:
            count+=1
        else:
            reduceChar+=currentChar+str(count)
            currentChar=s[i]
            count=1     

    reduceChar+=currentChar+str(count)
    return reduceChar        


string=input("enter a string: ")
output_str=reduceChar(string)
print(output_str)