#  String question - Remove all characters from string except alphabets
def removeChar(string):
    print(''.join(filter(str.isalpha,string)))

string="omkar433@@12abcd3"
removeChar(string)