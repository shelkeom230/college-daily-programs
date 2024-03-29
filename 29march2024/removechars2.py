# using list comprehension 
def removeChars(string):
    result=[ele for ele in string if ele.isalpha()]
    print(''.join(result))

removeChars('omkar12342@##@@abcdefhg')