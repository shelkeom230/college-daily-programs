# 15. Program to find string is anagram or not.
def findAnagram(str1,str2):
    str1_lower=str1.lower().replace(" ","")
    str2_lower=str2.lower().replace(" ","")

    if len(str1_lower)!=len(str2_lower):
        return 'not anagram'

    
    sorted1=sorted(str1)
    sorted2=sorted(str2)

    if sorted1==sorted2:
        return 'anagram'
    else:
        return 'not anagram'


str1="omkar"
str2="substring"
print(findAnagram(str1,str2))

