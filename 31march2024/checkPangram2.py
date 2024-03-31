# using list comprehension
def checkPangram(string): 
    string_lower=string.lower().replace(" ","")
    alphabets='abcdefghijklmnopqrstuvwxyz'

    print('yes' if all(char in string_lower for char in alphabets) else 'no')

checkPangram('the quick brown fox jumps over the lazy dog')
