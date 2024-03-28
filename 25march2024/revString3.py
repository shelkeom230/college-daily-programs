# using loop 
def revStr(string):
    rev_str=''

    for char in string:
        rev_str=char+rev_str
    return rev_str

string=input("enter a string: ")   
print(revStr(string))