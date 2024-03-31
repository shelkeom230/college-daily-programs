# 16. Program to check string is pangram or not
def checkPangram(string):
    string_lower=string.lower().replace(" ","")

    alphabets="abcdefghijklmnopqrstuvwxyz"

    for char in alphabets:
        if char not in string_lower:
            return False 
        
    return True 

print(checkPangram('Pack my box with five dozen liquor jugs'))

