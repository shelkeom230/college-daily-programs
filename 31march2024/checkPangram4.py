# using regular expressoin 
import re 

def checkPangram(string):
    return len(set(re.findall("[a-z]",string.lower())))==26

print(checkPangram('the quick brown fox jumps over the lazy dog'))