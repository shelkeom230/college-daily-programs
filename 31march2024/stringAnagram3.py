# using sorted function directly in our return 
def checkAnagram(str1,str2):
    str1_lower=str1.lower().replace(" ","")
    str2_lower=str2.lower().replace(" ","")

    return sorted(str1_lower)==sorted(str2_lower)

if checkAnagram('omkar','aromkar'):
    print('yes')
else:
    print('no')