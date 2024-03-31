# using collections.counter 
from collections import Counter
def checkAnagram(str1,str2):
    str1_lower=str1.lower().replace(" ","")
    str2_lower=str2.lower().replace(" ","")

    return Counter(str1)==Counter(str2)

print('yes' if checkAnagram('omkar','karom') else 'no')