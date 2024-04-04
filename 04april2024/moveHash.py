# move all hashes in string to the start and reutrn the string 
# take input of string from user 
def moveHashes(string):
    hash_count=string.count('#')
    string=[ele for ele in string if ele!='#']
    result=['#']*hash_count+string
    return ''.join(result)

string=input("enter a string: ")
print(moveHashes(string))

